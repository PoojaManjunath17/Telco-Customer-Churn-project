import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Customer LTV Dashboard")

df = pd.read_csv("feature_engineered_telco.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Monthly Charges Distribution")

fig = px.histogram(
    df,
    x="MonthlyCharges"
)

st.plotly_chart(fig)

st.subheader("Tenure Analysis")

fig2 = px.scatter(
    df,
    x="tenure",
    y="MonthlyCharges"
)

st.plotly_chart(fig2)