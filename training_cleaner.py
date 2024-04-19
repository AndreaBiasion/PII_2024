import json
from datetime import datetime, timedelta, timezone
import matplotlib.pyplot as plt

class DataProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.new_data = None
        self.keywords_counter = None
        self.total_words_counter = None
        self.start_date = None
        self.end_date = None
        self.interval = None
        self.span = None

    def load_data(self):
        with open(self.filename, 'r') as file:
            # Load the JSON data
            data = json.load(file)

        self.new_data = {}
        for date_str, text in data.items():
            if text.strip():  # Check if text is not empty or just whitespace
                self.new_data[date_str] = text

    def process_data(self, start_date, end_date):
        self.start_date = start_date.replace(tzinfo=timezone.utc)
        self.end_date = end_date.replace(tzinfo=timezone.utc)

        # Define the interval (6 hours)
        self.interval = timedelta(hours=6)

        # Calculate the difference in hours between the two dates
        difference_hours = (self.end_date - self.start_date).total_seconds() / 3600

        # Calculate the number of 6-hour intervals
        self.span = difference_hours / 6

        # Initialize counters
        self.keywords_counter = {'earthquake': [0]*int(self.span), 'quake': [0]*int(self.span), 'shock': [0]*int(self.span)}
        self.total_words_counter = [0]*int(self.span)

        # Iterate through the data in 6-hour intervals
        pos = 0
        current_date = self.start_date
        while current_date <= self.end_date and pos < int(self.span):
            next_date = current_date + self.interval

            # Count occurrences of keywords and total words within the current interval
            for date_str, text in self.new_data.items():
                date = datetime.fromisoformat(date_str).replace(tzinfo=timezone.utc)
                if current_date <= date < next_date:
                    for word in self.keywords_counter.keys():
                        if word in text:
                            self.keywords_counter[word][pos] += 1
                    self.total_words_counter[pos] += len(text.split())

            # Move to the next interval
            current_date = next_date
            pos += 1


class DataPlotter:
    def __init__(self, processor):
        self.processor = processor

    def plot_data(self):
        timeline = [self.processor.start_date + i * self.processor.interval for i in range(int(self.processor.span))]  # Timeline of intervals
        keywords = list(self.processor.keywords_counter.keys())  # List of keywords

        # Plot keyword frequencies over time
        plt.figure(figsize=(12, 6))
        for keyword in keywords:
            plt.plot(timeline, self.processor.keywords_counter[keyword], label=keyword)

        # Add labels and legend
        plt.title('Keyword Frequencies Over Time')
        plt.xlabel('Time')
        plt.ylabel('Frequency')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Show plot
        plt.show()


# Usage example
processor = DataProcessor('cleaned_datasets/al_jazeera_clean.json')
processor.load_data()
processor.process_data(datetime(2023, 9, 6, 0, 0, 0), datetime(2024, 3, 29, 23, 59, 0))

plotter = DataPlotter(processor)
plotter.plot_data()
