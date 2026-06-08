import joblib
import pandas as pd

model = joblib.load("customer_ltv_model.pkl")

new_customer = pd.DataFrame({
    "tenure": [24],
    "MonthlyCharges": [75]
})

prediction = model.predict(new_customer)

print("Predicted LTV:", prediction[0]
