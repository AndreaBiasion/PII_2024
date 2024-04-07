# This script is used for cleaning fetched data, removing unnecessary characters, stopwords, and converting text to lowercase.

import json
import string
from nltk.corpus import stopwords
from pickle import dump

# List of keywords to filter messages
keywords = ['biden']

# Function to load JSON data from a file
def load_doc(filename):
    """
    Load JSON data from the specified file.

    Args:
        filename (str): The name of the file to load.

    Returns:
        dict: A dictionary containing messages with dates as keys and corresponding text as values.
    """
    with open(filename, 'r') as file:
        # Load the JSON data
        data = json.load(file)

    messages = {}
    for item in data:
        # Check if the dictionary has 'date' and 'text' keys and if the values are not None
        if 'date' in item and 'text' in item and item['text'] is not None and item['date'] is not None:
            # Store messages with their corresponding dates
            messages[item['date']] = item['text']

    return messages

# Function to clean text data
def clean_text(text):
    """
    Clean text data by removing punctuation, stopwords, and converting to lowercase.

    Args:
        text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    tokens = text.split()
    table = str.maketrans('', '', string.punctuation)

    tokens = [w.translate(table) for w in tokens]
    stop_words = set(stopwords.words('english'))

    tokens = [w for w in tokens if not w in stop_words]
    tokens = [word for word in tokens if len(word) > 2]
    tokens = ' '.join(tokens).lower()

    return tokens

# Function to clean the entire dataset
def clean_dataset(dataset):
    """
    Clean the entire dataset by applying clean_text function to each message.

    Args:
        dataset (dict): The dataset containing messages with dates as keys and corresponding text as values.

    Returns:
        dict: The cleaned dataset.
    """
    for date, text in dataset.items():
        dataset[date] = clean_text(text)
    return dataset

# Function to save the cleaned dataset to a file
def save_dataset(dataset, filename):
    """
    Save the cleaned dataset to a JSON file.

    Args:
        dataset (dict): The cleaned dataset to be saved.
        filename (str): The name of the file to save the dataset to.
    """
    # Save messages to a JSON file
    with open(filename, 'w') as f:
        json.dump(dataset, f, indent=4)
        print('Saved dataset')
