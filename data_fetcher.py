# For this code we took inspiration from:
# https://medium.com/@chodvadiyasaurabh/automating-data-collection-and-analysis-from-telegram-groups-using-python-and-telethon-8d51e194fa8b

import asyncio
import json
from datetime import datetime, timedelta
from pytz import UTC
from telethon import TelegramClient, errors
import time


# Replace the values with your own API_ID, API_HASH, PHONE_NUMBER
api_id = "22359680"
api_hash = "ec56214c6844908edfa17c4cc6778a1c"
phone_number = "+393455294953"

# Enter group id -100 after the digit
group_name = -1001562033113

messages = []


async def fetch_messages(client, entity, start_date, end_date, message_limit):
    """
    Asynchronously fetch messages from the specified Telegram group within the given date range and message limit.

    :param client: TelegramClient instance.
    :param entity: Telegram group entity.
    :param start_date: Start date for message retrieval (datetime object).
    :param end_date: End date for message retrieval (datetime object).
    :param message_limit: Maximum number of messages to retrieve.
    """

    try:
        batch_size = 100  # Adjust batch size as needed
        processed_messages = 0

        while processed_messages < message_limit:
            # Fetch messages in batches
            messages_batch = await client.get_messages(entity, limit=batch_size, offset_date=end_date)

            # Filter messages within the desired date range
            relevant_messages = [msg for msg in messages_batch
                                 if start_date <= msg.date.replace(tzinfo=None) <= end_date.replace(tzinfo=None)]

            # Handle relevant messages
            for message in relevant_messages:
                handle_message(message)

                processed_messages += 1

                # Check if message limit is reached
                if processed_messages >= message_limit:
                    break

            # Update end_date for the next batch
            if messages_batch:
                end_date = messages_batch[-1].date - timedelta(seconds=1)

    except errors.FloodWaitError as e:
        print(f"API Flood limit. Waiting for {e.seconds} seconds.")
        await asyncio.sleep(e.seconds)
        await fetch_messages(client, entity, start_date, end_date, message_limit - processed_messages)


async def main():
    """
    Main entry point of the script. Establishes a connection with the Telegram client,
    retrieves the group entity, and initiates message fetching.
    """
    start_time = time.time()  # Record start time
    async with TelegramClient('session_name', api_id, api_hash) as client:
        entity = await client.get_entity(group_name)
        start_date = datetime(2024, 3, 1).replace(tzinfo=None)  # Making start_date timezone-naive
        end_date = datetime(2024, 3, 13, tzinfo=UTC)
        message_limit = 500
        await fetch_messages(client, entity, start_date, end_date, message_limit)
    end_time = time.time()  # Record end time
    print(f"Execution time: {end_time - start_time} seconds")


def handle_message(message):
    """
    Processes each fetched message and appends its details to the messages list.

    :param message: Telegram message object.
    """
    messages.append({
        'id': message.id,
        'date': message.date.isoformat(),
        'text': message.text
        # Add more fields as needed
    })


# Run the event loop
asyncio.run(main())

# Save messages to a JSON file
with open('messages.json', 'w') as f:
    json.dump(messages, f, indent=4)
