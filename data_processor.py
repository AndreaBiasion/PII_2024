import json
from datetime import datetime, timedelta, timezone


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
        self.normalized_vector = None

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
        self.keywords_counter = {'earthquake': [0] * int(self.span), 'quake': [0] * int(self.span),
                                 'shock': [0] * int(self.span), 'magnitude': [0] * int(self.span),
                                 'seismic': [0] * int(self.span), 'aftershock': [0] * int(self.span),
                                 'fault': [0] * int(self.span), 'tectonic plates': [0] * int(self.span),
                                 'epicenter': [0] * int(self.span), 'richter scale': [0] * int(self.span),
                                 'seismograph': [0] * int(self.span), 'seismology': [0] * int(self.span),
                                 'seismic waves': [0] * int(self.span)}

        self.total_words_counter = [0] * int(self.span)

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

        for key, value in self.keywords_counter.items():
            for i in range(0, len(self.total_words_counter)):
                if self.total_words_counter[i] != 0:
                    value[i] = value[i] / self.total_words_counter[i]

        self.normalized_vector = [0] * len(self.total_words_counter)

        for key, value in self.keywords_counter.items():
            #print(key, value)
            for i in range(0, len(self.normalized_vector)):
                self.normalized_vector[i] += value[i]

        #for i in range(0, len(self.normalized_vector)):
            #print(self.normalized_vector[i])
