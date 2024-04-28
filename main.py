# print("Work in progress...")
from DecisionTree import *
from TrueOccurences import *
from data_cleaner import *
from data_plotter import *
from data_processor import *
from detector import *
import numpy as np


def check_precision(filename, detector, start_date, end_date):
    findRealEarthquake = TrueOccurences()
    earthquake_occurrences = findRealEarthquake.findOccurences(filename, start_date, end_date)

    TP = 0
    FP = 0
    FN = 0

    TP = sum((gt == 1) and (pred == 1) for gt, pred in zip(earthquake_occurrences, detector.vector))
    FP = sum((gt == 0) and (pred == 1) for gt, pred in zip(earthquake_occurrences, detector.vector))
    FN = sum((gt == 1) and (pred == 0) for gt, pred in zip(earthquake_occurrences, detector.vector))

    print(f'Precision: {TP / (TP + FP) * 100:.2f}%')
    print(f'Recall: {TP / (TP + FN) * 100:.2f}%')


# dataset = load_doc('datasets/raw_datasets/rtnews_group_data.json')

# dataset = clean_dataset(dataset)

print("Cleaned dataset")

# save_dataset(dataset, 'datasets/cleaned_datasets/rtnews_group_data_clean.json')

clean_dataset = 'datasets/cleaned_datasets/al_jazeera_clean.json'

# Usage example
processor = DataProcessor(clean_dataset)
processor.load_data()

start_date = datetime(2023, 1, 1, 5, 0, 0)
end_date = datetime(2023, 3, 30, 23, 59, 0)

processor.process_data(start_date, end_date)

detector = Detector()

detector.detect(processor)

plotter = DataPlotter(processor, detector)
plotter.plot_data()

check_precision('datasets/events_dataset/query.geojson.json', detector, start_date, end_date)

decisiontree = DecisionTree()

trueocc = TrueOccurences()

matrix = np.array([v for v in processor.keywords_counter.values()]).reshape(-1, 13)
label = trueocc.findOccurences('datasets/events_dataset/query.geojson.json', start_date, end_date)

decisiontree.classify(matrix, label)
