# This will be used in the future.

print("Work in progress...")

from data_cleaner import *
from data_plotter import *
from data_processor import *
from detector import *

dataset = load_doc('datasets/raw_datasets/aljazeera.json')

dataset = clean_dataset(dataset)

print("Cleaned dataset")

save_dataset(dataset, 'datasets/cleaned_datasets/al_jazeera_clean.json')

# Usage example
processor = DataProcessor('datasets/cleaned_datasets/al_jazeera_clean.json')
processor.load_data()
processor.process_data(datetime(2023, 3, 28, 18, 0, 0), datetime(2024, 3, 29, 23, 59, 0))

detector = Detector()

detector.detect(processor)

plotter = DataPlotter(processor, detector)
plotter.plot_data()
