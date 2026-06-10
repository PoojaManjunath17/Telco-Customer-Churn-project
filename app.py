from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("customer_ltv_model.pkl")


@app.post("/predict")
def predict(customer: dict):
    data = pd.DataFrame([customer])

    prediction = model.predict(data)

    return {
        "Predicted_LTV": float(prediction[0])
    }


@app.post("/batch_predict")
def batch_predict():
    df = pd.read_csv("batch_input.csv")

    predictions = model.predict(df)

    return dict(predictions=predictions.tolist())
