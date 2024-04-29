import json
from datetime import datetime, timedelta, timezone


class TrueOccurences:

    def __init__(self):
        self.earthquake_occurrences = None
        self.interval = None
        self.earthquake_features = None

    def findOccurences(self, filename, start_date, end_date):
        with open(filename, "r") as f:
            data = json.load(f)

            self.earthquake_features = data["features"]

            start_date = start_date.replace(tzinfo=timezone.utc)
            end_date = end_date.replace(tzinfo=timezone.utc)

            self.interval = timedelta(hours=6)

            self.earthquake_occurrences = [0] * int(((end_date - start_date).total_seconds() / 3600) / 6)
            current_date = start_date
            pos = 0
            while current_date <= end_date:
                # Check if there's an earthquake recorded within the current interval
                for feature in self.earthquake_features:
                    properties = feature["properties"]
                    time = properties["time"] / 1000  # Convert milliseconds to seconds
                    earthquake_date = datetime.fromtimestamp(time, tz=timezone.utc)
                    if current_date <= earthquake_date < current_date + self.interval:
                        self.earthquake_occurrences[pos] = 1

                pos += 1
                # Move to the next interval
                current_date += self.interval

        return self.earthquake_occurrences
