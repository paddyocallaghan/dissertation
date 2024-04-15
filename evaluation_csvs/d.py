import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the similarity scores CSV
df = pd.read_csv("similarity_scores.csv")

# Calculate descriptive statistics for each property
descriptive_stats = df.describe()

# Calculate the overall average similarity score
overall_avg_score = df.iloc[:, 1:].mean().mean()

# Calculate the average similarity score for each property
avg_score_by_property = df.iloc[:, 1:].mean()

# Calculate the average similarity score for each incident
avg_score_by_incident = df.iloc[:, 1:].mean(axis=1)

# Print the descriptive statistics
print("Descriptive Statistics for Each Property:")
print(descriptive_stats)

# Print the overall average similarity score
print(f"\nOverall Average Similarity Score: {overall_avg_score}")

# Print the average similarity score by property
print("\nAverage Similarity Score by Property:")
print(avg_score_by_property)

# Print the average similarity score by incident
print("\nAverage Similarity Score by Incident:")
print(avg_score_by_incident)

# Plotting the average similarity score by property
plt.figure(figsize=(10, 6))
avg_score_by_property.plot(kind="bar")
plt.title("Average Similarity Score by Property")
plt.xlabel("Property")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plotting the average similarity score by incident
plt.figure(figsize=(12, 6))
avg_score_by_incident.plot(kind="line", marker="o")
plt.title("Average Similarity Score by Incident")
plt.xlabel("Incident")
plt.ylabel("Average Score")
plt.grid(True)
plt.tight_layout()
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the similarity scores CSV
df = pd.read_csv("similarity_scores.csv")

# Drop the 'incidentNo' column to focus on the properties
df.drop("incidentNo", axis=1, inplace=True)

# Calculate the average similarity score for each property
avg_scores = df.mean(axis=0).sort_values(ascending=False)

# Convert the Series to a DataFrame for plotting
avg_scores_df = avg_scores.to_frame(name="Average Similarity Score").transpose()

# Plotting the heatmap
plt.figure(figsize=(10, 4))
sns.heatmap(
    avg_scores_df,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    cbar_kws={"label": "Average Similarity Score"},
)
plt.title("Average Similarity Scores by Property")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


import pandas as pd

# Load the similarity scores CSV
df = pd.read_csv("similarity_scores.csv")

# Calculate descriptive statistics for each property
descriptive_stats = df.describe()

# Calculate the overall average similarity score
overall_avg_score = df.mean().mean()

# Calculate the average similarity score for each property
avg_score_by_property = df.mean()

# Calculate the average similarity score for each incident
avg_score_by_incident = df.mean(axis=1)

# Print the descriptive statistics
print("Descriptive Statistics for Each Property:")
print(descriptive_stats)

# Print the overall average similarity score
print(f"\nOverall Average Similarity Score: {overall_avg_score}")

# Print the average similarity score by property
print("\nAverage Similarity Score by Property:")
print(avg_score_by_property)

# Print the average similarity score by incident
print("\nAverage Similarity Score by Incident:")
print(avg_score_by_incident)
