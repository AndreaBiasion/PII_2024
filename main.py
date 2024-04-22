# This will be used in the future.

print("Work in progress...")

from data_cleaner import *
from data_plotter import *
from data_processor import *

dataset = load_doc('datasets/raw_datasets/aljazeera.json')

dataset = clean_dataset(dataset)

print("Cleaned dataset")
for date, text in dataset.items():
    for keyword in keywords:
        if keyword in text:
            print(f"Date: {date} Text: {text}")

save_dataset(dataset, 'datasets/cleaned_datasets/al_jazeera_clean.json')

# Usage example
processor = DataProcessor('datasets/cleaned_datasets/big_clean_data.json')
processor.load_data()
processor.process_data(datetime(2023, 9, 6, 0, 0, 0), datetime(2024, 3, 29, 23, 59, 0))

plotter = DataPlotter(processor)
plotter.plot_data()
