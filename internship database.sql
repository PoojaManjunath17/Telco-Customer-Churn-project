CREATE TABLE telco_customers (
customerID VARCHAR(50),
gender VARCHAR(20),
SeniorCitizen INT,
Partner VARCHAR(10),
Dependents VARCHAR(10),
tenure INT,
PhoneService VARCHAR(10),
MultipleLines VARCHAR(30),
InternetService VARCHAR(30),
OnlineSecurity VARCHAR(30),
OnlineBackup VARCHAR(30),
DeviceProtection VARCHAR(30),
TechSupport VARCHAR(30),
StreamingTV VARCHAR(30),
StreamingMovies VARCHAR(30),
Contract VARCHAR(30),
PaperlessBilling VARCHAR(10),
PaymentMethod VARCHAR(50),
MonthlyCharges FLOAT,
TotalCharges VARCHAR(50),
Churn VARCHAR(10));
SELECT COUNT(*) FROM telco_customers;
SELECT * 
FROM telco_customers
LIMIT 10;