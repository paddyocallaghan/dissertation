import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.impute import SimpleImputer

# Load the datasets
airo_gpt_df = pd.read_csv("evaluation_csvs/AIRO_GPT.csv")
airo_claude_df = pd.read_csv("evaluation_csvs/AIRO_Claude.csv")
cids_gpt_df = pd.read_csv("evaluation_csvs/CIDS_GPT.csv")
cids_claude_df = pd.read_csv("evaluation_csvs/CIDS_Claude.csv")

# Drop the first column (incident number) from each dataframe
airo_gpt = airo_gpt_df.drop(airo_gpt_df.columns[0], axis=1)
airo_claude = airo_claude_df.drop(airo_claude_df.columns[0], axis=1)
cids_gpt = cids_gpt_df.drop(cids_gpt_df.columns[0], axis=1)
cids_claude = cids_claude_df.drop(cids_claude_df.columns[0], axis=1)

airo_gpt.head()
airo_claude.head()
# Combine all datasets into one DataFrame
combined_df = pd.concat(
    [
        airo_gpt.assign(dataset="AIRO_GPT"),
        airo_claude.assign(dataset="AIRO_Claude"),
    ]
).reset_index(drop=True)

print(combined_df.head())
# Convert 'dataset' column to categorical type and then to dummy variables
combined_df = pd.get_dummies(combined_df, columns=["dataset"], drop_first=True)

# Separate the features (X) and the target (y)
X = combined_df.drop(
    "has_serverity", axis=1
)  # Assuming 'hasDescription' is the target variable
y = combined_df["has_serverity"]


# Impute missing values using SimpleImputer
imputer = SimpleImputer(strategy="median")
X_imputed = imputer.fit_transform(X)

# Split the imputed data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_imputed, y, test_size=0.3, random_state=42
)

# Initialize and train the logistic regression model
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

# Predict on the test set
y_pred = log_reg.predict(X_test)

# Evaluate the model
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
