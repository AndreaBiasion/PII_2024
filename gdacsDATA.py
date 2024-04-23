from gdacs.api import GDACSAPIReader
import json

# Initialize the GDACS API client
client = GDACSAPIReader()

# Fetch the latest earthquake events
eq_events = client.latest_events(event_type="EQ")

# Convert GeoJSON object to a dictionary
eq_events_dict = eq_events.dict()

# Access earthquake events
earthquake_events = eq_events_dict["features"]

# Iterate through each earthquake event and access the severity information
for event in earthquake_events:
    # Access the severity information if available
    if "severitydata" in event["properties"]:
        severity = event["properties"]["severitydata"]["severity"]
        print(f"Severity of event: {severity}")
    else:
        print("Severity data not found for this event")

# Write the earthquake events to a JSON file
with open('datasets/events_dataset/events.json', 'w') as f:
    json.dump(earthquake_events, f, indent=4)
