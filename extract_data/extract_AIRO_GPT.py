import re
import pandas as pd

# Define the properties to extract
properties = [
    "is applied within domain",
    "has purpose",
    "produces output",
    "has risk",
    "has consequence",
    "has impact",
    "has stakeholder",
    "mitigation",
    "is provided by",
    "has severity",
    "has likelihood",
]

# Initialize a dictionary to hold the data
data = {prop: [] for prop in properties}
data["incident"] = []

# Read the content of the file
with open("paste.txt", "r") as file:
    content = file.read()

# Split the content by incidents
incidents = content.split(":incident")

# Process each incident
for incident in incidents[1:]:  # Skip the first split as it's before the first incident
    incident_number = incident.split()[0]
    data["incident"].append(incident_number)

    # Extract the properties for each incident
    for prop in properties:
        # Create a regex pattern to match the property and capture its value
        pattern = f':{prop.replace(" ", "_")} "(.*?)" ;'
        match = re.search(pattern, incident, re.DOTALL)

        # If a match is found, add the value to the data dictionary
        if match:
            data[prop].append(match.group(1))
        else:
            # If no match is found, add a None or empty string
            data[prop].append(None)

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Set the incident number as the index
df.set_index("incident", inplace=True)

# Transpose the DataFrame to have properties on the x-axis and incident number on the y-axis
df = df.T

# Save the DataFrame to a CSV file
df.to_csv("extracted_properties.csv")

print(df)
