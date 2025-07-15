import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("heart_disease_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Heart Disease Risk Predictor", layout="centered")

# Header
st.markdown("<h1 style='text-align: center; color: red;'>❤️ Heart Disease Risk Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter your medical details to check your risk level</p>", unsafe_allow_html=True)
st.markdown("---")

# Layout with columns
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("🧓 Age", 20, 100, 50)
    sex = st.radio("⚧️ Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
    cp = st.selectbox("💥 Chest Pain Type (cp)", [0, 1, 2, 3])
    trestbps = st.number_input("🩺 Resting Blood Pressure", 80, 200, 120)
    chol = st.number_input("🧪 Serum Cholesterol (mg/dl)", 100, 600, 200)
    fbs = st.radio("🍬 Fasting Blood Sugar > 120?", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    restecg = st.selectbox("📈 Resting ECG", [0, 1, 2])

with col2:
    thalach = st.number_input("🏃 Max Heart Rate", 60, 220, 150)
    exang = st.radio("😓 Exercise-induced Angina", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    oldpeak = st.slider("📉 ST Depression (oldpeak)", 0.0, 6.0, 1.0, 0.1)
    slope = st.selectbox("🧗 Slope of ST Segment", [0, 1, 2])
    ca = st.selectbox("🩻 Major Vessels Colored", [0, 1, 2, 3])
    thal = st.selectbox("🧬 Thalassemia", [0, 1, 2, 3])  # typically 1=normal, 2=fixed, 3=reversible

# Submit button
st.markdown("---")
if st.button("🔍 Predict"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                            restecg, thalach, exang, oldpeak,
                            slope, ca, thal]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        st.error(f"⚠️ **High risk of heart disease!**\n\nProbability: **{probability:.2%}**")
    else:
        st.success(f"✅ **Low risk of heart disease.**\n\nProbability: **{probability:.2%}**")