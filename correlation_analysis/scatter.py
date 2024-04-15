import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame
df = pd.read_csv("s1.csv")

# Set figure size
plt.figure(figsize=(12, 8))

# Get a list of all features (assuming the first column is 'Incident')
features = df.columns[1:]

# Get a list of all incidents
incidents = df["Incident"]

# Iterate over each incident and plot its features
for incident in incidents:
    # Get the row corresponding to the current incident
    row = df[df["Incident"] == incident]
    for feature in features:
        # Check if the feature is present (1) for the current incident
        if row[feature].values[0] == 1:
            plt.scatter(
                incident, feature, alpha=0.5, color="blue"
            )  # All dots are now blue

# Set labels and title
plt.xlabel("Incidents")
plt.ylabel("Features")
plt.title("Feature Presence in Incidents")

# Rotate incident names for readability if necessary
plt.xticks(rotation=90)

# Show the plot
plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
plt.savefig("plt2.png")
