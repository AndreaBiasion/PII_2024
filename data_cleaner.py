# This is used for cleaning the fetched data

import json
import string
from nltk.corpus import stopwords
from pickle import dump


# TODO: check a new method for filtering messages --> war != warn but warn contains warn

# Open the file containing the JSON data
def load_doc(filename):
    with open('prova.json', 'r') as file:
        # Load the JSON data
        data = json.load(file)

    messages = []
    for item in data:
        # Check if the dictionary has a 'text' key
        if 'text' in item and item['text'] is not None:
            # Check if any of the keywords are present in the message text
                messages.append(item['text'])

    return messages



def clean_doc(data):
    data_string = json.dumps(data)
    tokens = data_string.split()
    table = str.maketrans('', '', string.punctuation)

    tokens = [w.translate(table) for w in tokens]
    stop_words = set(stopwords.words('english'))

    tokens = [w for w in tokens if not w in stop_words]
    tokens = [word for word in tokens if len(word) > 1]
    tokens = ' '.join(tokens)

    return tokens


def save_dataset(data, filename):
    dump(data, open(filename, 'wb'))
    print('Saved')


data = load_doc('prova.json')
tokens = clean_doc(data)
print(tokens)
