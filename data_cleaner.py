# This is used for cleaning the fetched data

import json

# TODO: check a new method for filtering messages --> war != warn but warn contains warn

# Open the file containing the JSON data
with open('messages.json', 'r') as file:
    # Load the JSON data
    data = json.load(file)

# Initialize an empty list to store filtered messages
filtered_messages = []

# Keywords to filter messages
keywords = ["war"]

# Check if data is a list of dictionaries
if isinstance(data, list):
    # Iterate through each dictionary in the list
    for item in data:
        # Check if the dictionary has a 'text' key
        if 'text' in item and item['text'] is not None:
            # Check if any of the keywords are present in the message text
            if any(keyword in item['text'] for keyword in keywords):
                # Append the message to the filtered messages list
                filtered_messages.append(item['text'])
else:
    # Check if data is a dictionary and has a 'text' key
    if isinstance(data, dict) and 'text' in data:
        # Check if any of the keywords are present in the message text
        if any(keyword in data['text'] for keyword in keywords):
            # Append the message to the filtered messages list
            filtered_messages.append(data['text'])

# Print the filtered messages
for message in filtered_messages:
    print(message)





