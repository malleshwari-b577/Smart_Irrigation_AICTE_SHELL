import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('Farm_Irrigation_System.pkl')

# Page configuration
st.set_page_config(page_title="🌿 Smart Sprinkler System 🌿", page_icon="💧", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #F0F8FF;
        }
        .subtitle {
            text-align: center;
            font-size: 22px;
            color: #6C3483;
            font-family: Arial, sans-serif;
            margin-top: 4px;
        }
        .credit {
            text-align: center;
            font-size: 18px;
            color: #2E8B57;
            font-style: italic;
            margin-bottom: 20px;
        }
        .sensor-section {
            font-size: 26px;
            color: #FF69B4;
            font-weight: bold;
            margin-top: 30px;
            margin-bottom: 10px;
        }
        .sprinkler-status {
            font-size: 18px;
            padding: 10px;
            margin: 8px 0;
            border-radius: 8px;
            background: #ffffff;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            transition: all 0.3s ease-in-out;
        }
        .sprinkler-status:hover {
            transform: scale(1.02);
            box-shadow: 2px 2px 15px rgba(0,0,0,0.2);
        }
    </style>
""", unsafe_allow_html=True)

# Main Title with gradient
st.markdown("""
    <h1 style='
        text-align: center;
        font-size: 60px;
        font-family: Verdana, Geneva, sans-serif;
        background: linear-gradient(to right, #00C9FF, #92FE9D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        margin-bottom: 0;
    '>
        🌿 Smart Sprinkler System 🌿
    </h1>
""", unsafe_allow_html=True)

# Subtitle and credit
st.markdown("<p class='subtitle'>Predict irrigation status using AI-powered sensors </p>", unsafe_allow_html=True)
st.markdown("<p class='credit'>AICTE Green AI Internship Project by <b>Bhimagoni Malleshwari</b></p>", unsafe_allow_html=True)

st.markdown("---")

# Sensor Input Section
st.markdown("<div class='sensor-section'>Sensor Inputs</div>", unsafe_allow_html=True)
sensor_values = []
cols = st.columns(5)

for i in range(20):
    with cols[i % 5]:
        val = st.slider(f'Sensor {i+1}', 0.0, 1.0, 0.5, 0.01)
        sensor_values.append(val)

st.markdown("---")

# Predict Button
center = st.columns([1, 2, 1])[1]
with center:
    if st.button("🔍 Predict Sprinkler Status"):
        input_array = np.array(sensor_values).reshape(1, -1)
        prediction = model.predict(input_array)[0]

        st.balloons()
        st.markdown("Prediction Results")
        st.success("Prediction successful! See the results below:")

        with st.expander("🔧 Sprinkler ON/OFF Details", expanded=True):
            for i, status in enumerate(prediction):
                color = "#32CD32" if status == 1 else "#FF4500"
                emoji = "ON" if status == 1 else "OFF"
                st.markdown(
                    f"<div class='sprinkler-status' style='border-left: 5px solid {color};'>"
                    f"<b>Sprinkler {i+1} (Parcel {i+1}):</b> {emoji}</div>",
                    unsafe_allow_html=True
                )

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; font-size:14px; color:#888;'>© 2025 Bhimagoni Malleshwari | Designed with ❤️ for Green AI 🌱</p>",
    unsafe_allow_html=True
)
