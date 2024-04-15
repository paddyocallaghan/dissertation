import pandas as pd
import re

# Define the properties to extract based on the provided ontology
properties = [
    "hasCatchmentArea",
    "hasDescription",
    "forOutcome",
    "intendedImpact",
    "hasConsequence",
    "forStakeholder",
    "hasMitigation",
    "fromPerspectiveOf",
    "hasImportance",
    "hasLikelihood",
]

# Initialize a dictionary to hold the data
data = {prop: [] for prop in properties}
data["incident"] = []

# Read the content of the file
with open("paste.txt", "r") as file:
    content = file.read()

# Split the content by incidents
incidents = re.split(r":incident\d+", content)

# Process each incident
for i, incident in enumerate(
    incidents[1:], start=1
):  # Skip the first split as it's before the first incident
    data["incident"].append(f"Incident{i}")

    # Extract the properties for each incident
    for prop in properties:
        # Create a regex pattern to match the property and capture its value
        pattern = rf":{prop} \"(.*?)\" ;"
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
df.to_csv("extracted_properties_paste.txt.csv")

print(df)
