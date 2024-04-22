from gdacs.api import GDACSAPIReader
import json

client = GDACSAPIReader()

# Fetch the latest earthquake events
eq_events = client.latest_events(event_type="EQ")

# Convert GeoJSON object to a dictionary
eq_events_dict = eq_events.dict()

# Write the earthquake events to a JSON file
with open('datasets/events_dataset/events.json', 'w') as f:
    json.dump(eq_events_dict, f, indent=4)
