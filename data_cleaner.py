# This is used for cleaning the fetched data

import json

# Open the file containing the JSON data
with open('messages.json', 'r') as file:
    # Load the JSON data
    data = json.load(file)

# Initialize an empty list to store messages
messages = []

# Check if data is a list of dictionaries
if isinstance(data, list):
    # Iterate through each dictionary in the list
    for item in data:
        # Check if the dictionary has a 'message' key
        if 'text' in item:
            # Append the value of the 'message' key to the messages list
            messages.append(item['text'])
else:
    # Check if data is a dictionary and has a 'message' key
    if isinstance(data, dict) and 'text' in data:
        # Append the value of the 'message' key to the messages list
        messages.append(data['text'])

# e.g: print the extracted messages
print(len(messages))

