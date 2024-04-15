import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets with updated paths
airo_gpt_df = pd.read_csv("evaluation_csvs/AIRO_GPT.csv")
airo_claude_df = pd.read_csv("evaluation_csvs/AIRO_Claude.csv")
cids_gpt_df = pd.read_csv("evaluation_csvs/CIDS_GPT.csv")
cids_claude_df = pd.read_csv("evaluation_csvs/CIDS_Claude.csv")

# Drop the first column (incident number) from each dataframe
airo_gpt = airo_gpt_df.drop(airo_gpt_df.columns[0], axis=1)
airo_claude = airo_claude_df.drop(airo_claude_df.columns[0], axis=1)
cids_gpt = cids_gpt_df.drop(cids_gpt_df.columns[0], axis=1)
cids_claude = cids_claude_df.drop(cids_claude_df.columns[0], axis=1)

# Calculate frequencies for each dataset
freq_airo_gpt = airo_gpt.sum()
freq_airo_claude = airo_claude.sum()
freq_cids_gpt = cids_gpt.sum()
freq_cids_claude = cids_claude.sum()

# Combine frequencies into separate DataFrames for AIRO and CIDS
frequencies_airo = pd.DataFrame(
    {"AIRO_GPT": freq_airo_gpt, "AIRO_Claude": freq_airo_claude}
)

frequencies_cids = pd.DataFrame(
    {"CIDS_GPT": freq_cids_gpt, "CIDS_Claude": freq_cids_claude}
)

# Plotting bar chart for AIRO frequencies
frequencies_airo.plot(kind="bar", figsize=(14, 7))
plt.title("Frequency of AIRO Annotations Across LLMs")
plt.xlabel("Property")
plt.ylabel("Frequency")
plt.xticks(rotation=90)
plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
plt.show()

# Plotting bar chart for CIDS frequencies
frequencies_cids.plot(kind="bar", figsize=(14, 7))
plt.title("Frequency of CIDS Annotations Across LLMs")
plt.xlabel("Property")
plt.ylabel("Frequency")
plt.xticks(rotation=90)
plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
plt.show()

# Creating a heatmap for the AIRO frequencies
sns.heatmap(frequencies_airo.T, annot=True, fmt="d", cmap="viridis")
plt.title("Heatmap of AIRO Annotation Frequencies")
plt.xticks(rotation=90)
plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
plt.show()

# Creating a heatmap for the CIDS frequencies
sns.heatmap(frequencies_cids.T, annot=True, fmt="d", cmap="viridis")
plt.title("Heatmap of CIDS Annotation Frequencies")
plt.xticks(rotation=90)
plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
plt.show()
