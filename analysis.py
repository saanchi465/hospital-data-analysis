import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\navee\Desktop\saanchi\Intern\hospital data analysis.csv")

# Show first rows
print(df.head())

# Dataset info
print(df.info())

# Missing values
print(df.isnull().sum())

# Fill missing values
for column in df.columns:
    if df[column].dtype == 'object':
        df[column] = df[column].fillna('Unknown')
    else:
        df[column] = df[column].fillna(df[column].mean())

# ----------------------------
# GENDER DISTRIBUTION
# ----------------------------

plt.figure(figsize=(6, 4))

sns.countplot(x='Gender', data=df)

plt.title('Gender Distribution')

plt.show()

# ----------------------------
# CONDITION ANALYSIS
# ----------------------------

plt.figure(figsize=(10, 5))

sns.countplot(
    y='Condition',
    data=df,
    order=df['Condition'].value_counts().index
)

plt.title('Most Common Conditions')

plt.show()

# ----------------------------
# AGE DISTRIBUTION
# ----------------------------

plt.figure(figsize=(8, 5))

sns.histplot(df['Age'], bins=20)

plt.title('Patient Age Distribution')

plt.show()

# ----------------------------
# COST ANALYSIS
# ----------------------------

plt.figure(figsize=(10, 5))

sns.boxplot(x='Cost', data=df)

plt.title('Treatment Cost Distribution')

plt.show()

# ----------------------------
# PROCEDURE ANALYSIS
# ----------------------------

procedure_counts = df['Procedure'].value_counts()

print("\nProcedure Analysis:\n")

print(procedure_counts)

# ----------------------------
# OUTCOME ANALYSIS
# ----------------------------

outcome_counts = df['Outcome'].value_counts()

print("\nOutcome Analysis:\n")

print(outcome_counts)

# ----------------------------
# SATISFACTION ANALYSIS
# ----------------------------

plt.figure(figsize=(8, 5))

sns.histplot(df['Satisfaction'], bins=10)

plt.title('Patient Satisfaction')

plt.show()

print("\nHealthcare Analytics Completed Successfully!")