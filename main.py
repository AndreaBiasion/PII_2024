#print("Work in progress...")

from data_cleaner import *
from data_plotter import *
from data_processor import *
from detector import *


def check_precision(filename, detector, start_date, end_date):
    # Load the JSON file
    with open(filename, "r") as f:
        data = json.load(f)

    # Extract earthquake features
    earthquake_features = data["features"]  # Define your start date

    start_date = start_date.replace(tzinfo=timezone.utc)
    end_date = end_date.replace(tzinfo=timezone.utc)

    # Define the interval duration (6 hours)
    interval = timedelta(hours=6)

    # Create a list to store earthquake occurrence for each interval
    earthquake_occurrences = [0] * int(((end_date - start_date).total_seconds() / 3600) / 6)

    # Iterate over 6-hour intervals from the start date to the end date
    current_date = start_date
    pos = 0
    while current_date <= end_date:
        # Check if there's an earthquake recorded within the current interval
        for feature in earthquake_features:
            properties = feature["properties"]
            time = properties["time"] / 1000  # Convert milliseconds to seconds
            earthquake_date = datetime.fromtimestamp(time, tz=timezone.utc)
            if current_date <= earthquake_date < current_date + interval:
                earthquake_occurrences[pos] = 1

        pos += 1
        # Move to the next interval
        current_date += interval

        TP = 0
        FP = 0
        TN = 0

        # Calculate True Positives, False Positives, and False Negatives
        TP = sum((gt == 1) and (pred == 1) for gt, pred in zip(earthquake_occurrences, detector.vector))
        FP = sum((gt == 0) and (pred == 1) for gt, pred in zip(earthquake_occurrences, detector.vector))
        FN = sum((gt == 1) and (pred == 0) for gt, pred in zip(earthquake_occurrences, detector.vector))


    if TP + FP != 0:
        precision = TP / (TP + FP)
        print(f'Precision: {precision * 100:.2f}%')
    else:
       print('precision not valid')

    if TP + FN != 0:
        recall = TP / (TP + FN)
        print(f'Recall: {recall * 100:.2f}%')
    else:
        print('recall not valid')



#dataset = load_doc('datasets/raw_datasets/rtnews_group_data.json')

#dataset = clean_dataset(dataset)

print("Cleaned dataset")

#save_dataset(dataset, 'datasets/cleaned_datasets/rtnews_group_data_clean.json')

# Usage example
processor = DataProcessor('datasets/cleaned_datasets/rtnews_group_data_clean.json')
processor.load_data()

start_date = datetime(2023, 1, 1, 5, 0, 0)
end_date = datetime(2023, 12, 30, 23, 59, 0)

processor.process_data(start_date, end_date)

detector = Detector()

detector.detect(processor)

plotter = DataPlotter(processor, detector)
plotter.plot_data()

check_precision('datasets/events_dataset/query.geojson.json',
                detector, start_date, end_date)
