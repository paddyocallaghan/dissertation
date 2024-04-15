import pandas as pd
import rdflib


# Function to parse a Turtle (.ttl) file and return a dictionary of features
def parse_turtle_file(turtle_file_path):
    # Initialize a graph
    g = rdflib.Graph()
    # Parse the Turtle file
    g.parse(turtle_file_path, format="turtle")

    # Define the namespace
    airo = rdflib.Namespace("https://w3id.org/airo#")

    # Initialize a dictionary to hold feature presence (1 or 0)
    features_dict = {}

    # Iterate over all features in the ontology
    for feature in g.predicates():
        # Convert the feature URI to a string and extract the local name
        feature_name = str(feature).split("#")[-1]
        # Check if the feature is present in the incident
        features_dict[feature_name] = 1 if (None, feature, None) in g else 0

    return features_dict


# Function to update the CSV file with a new incident
def update_csv_with_incident(csv_file_path, incident_name, incident_features_dict):
    # Load the existing CSV file into a DataFrame
    df = pd.read_csv(csv_file_path, index_col="Incident")

    # Add the new incident to the DataFrame
    df.loc[incident_name] = incident_features_dict

    # Save the updated DataFrame back to CSV
    df.to_csv(csv_file_path)


# Path to your Turtle file and CSV file
turtle_file_path = "zAIRO_RDF/i1F.ttl"
csv_file_path = "s1.csv"

# Parse the Turtle file to get the features for the new incident
incident_name = "diff2"  # Replace with your incident name
incident_features_dict = parse_turtle_file(turtle_file_path)

# Update the CSV file with the new incident
update_csv_with_incident(csv_file_path, incident_name, incident_features_dict)
