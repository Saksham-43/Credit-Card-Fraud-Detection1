import streamlit as st
import numpy as np
import joblib
import random

# Load trained model
model = joblib.load("xgboost_fraud_model.pkl")

st.title("💳 Credit Card Fraud Detection")

st.write("Enter transaction details or generate a random transaction.")

# Manual inputs
time = st.number_input("Transaction Time", min_value=0.0)
amount = st.number_input("Transaction Amount", min_value=0.0)

# Random transaction button
if st.button("Generate Random Transaction"):
    
    time = random.randint(0, 172000)
    amount = round(random.uniform(1, 2000), 2)

    st.write("Generated Transaction")
    st.write(f"Time: {time}")
    st.write(f"Amount: {amount}")

# Prediction button
if st.button("Predict Fraud"):

    features = np.zeros(30)
    features[0] = time
    features[29] = amount

    features = features.reshape(1, -1)

    prediction = model.predict(features)
    probability = model.predict_proba(features)[0][1]

    if prediction[0] == 1:
        st.error(f"🚨 Fraudulent Transaction\nFraud Probability: {probability:.4f}")
    else:
        st.success(f"✅ Normal Transaction\nFraud Probability: {probability:.4f}")