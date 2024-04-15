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

# Combine frequencies into a single DataFrame
frequencies = pd.DataFrame(
    {
        "AIRO_GPT": freq_airo_gpt,
        "AIRO_Claude": freq_airo_claude,
        "CIDS_GPT": freq_cids_gpt,
        "CIDS_Claude": freq_cids_claude,
    }
)

# Plotting frequencies for each LLM and ontology
frequencies.plot(kind="bar", figsize=(5, 5))
plt.title("Frequency of Annotations Across LLMs and Ontologies")
plt.xlabel("Property")
plt.ylabel("Frequency")
plt.show()

# Creating a heatmap for the frequencies
sns.heatmap(frequencies, annot=True, cmap="viridis")
plt.title("Heatmap of Annotation Frequencies")
plt.show()
