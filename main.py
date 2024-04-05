# This will be used in the future.

print("Work in progress...")

from data_cleaner import *

dataset = load_doc('datasets/prova.json')

dataset = clean_dataset(dataset)

for date, text in dataset.items():
    for keyword in keywords:
        if keyword in text:
            print(f"Date: {date} Text: {text}")

save_dataset(dataset, 'cleaned_datasets/clean_data.json')
