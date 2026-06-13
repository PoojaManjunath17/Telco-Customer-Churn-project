import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv(r"C:\Users\Admin\OneDrive\Desktop\internship\feature_engineered_telco.csv")

# Features and target
X = df[["tenure"]]
y = df["MonthlyCharges"]

# Train model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "customer_ltv_model.pkl")

print("Model saved successfully!")