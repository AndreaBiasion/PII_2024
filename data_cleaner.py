# This is used for cleaning the fetched data

import json
import string
from nltk.corpus import stopwords
from pickle import dump

keywords = ['biden ']


# Open the file containing the JSON data
def load_doc(filename):
    with open(filename, 'r') as file:
        # Load the JSON data
        data = json.load(file)

    messages = {}
    for item in data:
        # Check if the dictionary has a 'text' key
        if 'date' in item and 'text' in item and item['text'] is not None and item['date'] is not None:
            # Check if any of the keywords are present in the message text
            messages[item['date']] = item['text']

    return messages


def clean_text(text):
    # data_string = json.dumps(text)
    tokens = text.split()
    table = str.maketrans('', '', string.punctuation)

    tokens = [w.translate(table) for w in tokens]
    stop_words = set(stopwords.words('english'))

    tokens = [w for w in tokens if not w in stop_words]
    tokens = [word for word in tokens if len(word) > 2]
    tokens = ' '.join(tokens).lower()

    return tokens


def clean_dataset(dataset):
    for date, text in dataset.items():
        dataset[date] = clean_text(text)
    return dataset


def save_dataset(dataset, filename):
    # Save messages to a JSON file
    with open(filename, 'w') as f:
        json.dump(dataset, f, indent=4)
        print('Saved dataset')
