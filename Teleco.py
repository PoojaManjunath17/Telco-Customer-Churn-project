import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Show first 5 rows
print(df.head())

# Dataset info
print(df.info())

# Check null values
print(df.isnull().sum())

# Convert TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Remove null rows
df.dropna(inplace=True)

# Churn count
sns.countplot(x='Churn', data=df)
plt.title("Customer Churn Count")
plt.show()

# Contract Type vs Churn
sns.countplot(x='Contract', hue='Churn', data=df)
plt.title("Contract Type vs Churn")
plt.show()

# Tenure vs Churn
sns.boxplot(x='Churn', y='tenure', data=df)
plt.title("Tenure vs Churn")
plt.show()

# Monthly Charges vs Churn
sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title("Monthly Charges vs Churn")
plt.show()

# Convert churn column
df['Churn'] = df['Churn'].map({'Yes':1, 'No':0})

# Correlation Heatmap
numeric_df = df.select_dtypes(include=['int64', 'float64'])

corr = numeric_df.corr()

plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap='coolwarm')

plt.title("Correlation Heatmap")
plt.show()

print("EDA Completed Successfully")

print("\nMissing Values:")
print(df.isnull().sum())

from sklearn.preprocessing import LabelEncoder

# Create encoder object
le = LabelEncoder()

# Encode all object columns
for column in df.select_dtypes(include=['object', 'string']).columns:
    df[column] = le.fit_transform(df[column])

print("\nCategorical Variables Encoded Successfully")

print("\nDataset Statistics:")
print(df.describe())

print("\nChurn Distribution:")
print(df['Churn'].value_counts())

print("\nAverage Monthly Charges:")
print(df['MonthlyCharges'].mean())

print("\nAverage Customer Tenure:")
print(df['tenure'].mean())

df.to_csv("cleaned_telco_churn.csv", index=False)

print("\nCleaned Dataset Saved Successfully")

# Average Charge Per Month
df['AvgChargePerMonth'] = df['TotalCharges'] / (df['tenure'] + 1)

# Total Services Used
service_columns = [
    'PhoneService',
    'MultipleLines',
    'InternetService',
    'OnlineSecurity',
    'OnlineBackup',
    'DeviceProtection',
    'TechSupport',
    'StreamingTV',
    'StreamingMovies'
]

df['TotalServices'] = df[service_columns].sum(axis=1)

print("\nFeature Engineering Completed")
