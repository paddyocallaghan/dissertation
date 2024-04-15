import pandas as pd
import rdflib


def parse_turtle_file(turtle_file_path):
    g = rdflib.Graph()
    g.parse(turtle_file_path, format="turtle")

    # Define the namespace
    airo = rdflib.Namespace("https://w3id.org/airo#")

    features_dict = {}
    # Iterate over all predicates in the graph and check their presence
    for feature in set(g.predicates()):
        feature_name = (
            feature.split("#")[-1] if "#" in feature else feature.split("/")[-1]
        )
        # Check if the feature is present in the graph
        features_dict[feature_name] = 1 if (None, feature, None) in g else 0

    return features_dict


def update_csv_with_incident(csv_file_path, incident_name, incident_features_dict):
    try:
        df = pd.read_csv(csv_file_path, index_col="Incident")
    except FileNotFoundError:
        # If the file does not exist, create a new DataFrame
        df = pd.DataFrame(columns=incident_features_dict.keys())
        df.index.name = "Incident"

    df.loc[incident_name] = incident_features_dict
    df.to_csv(csv_file_path)


# Paths to your Turtle file and CSV file
turtle_file_path = "AIRO_50.ttl"
csv_file_path = "sx.csv"

# Parse the Turtle file to get the features for the new incident
incident_name = "1"  # Replace with your incident name
incident_features_dict = parse_turtle_file(turtle_file_path)

# Update the CSV file with the new incident
update_csv_with_incident(csv_file_path, incident_name, incident_features_dict)
