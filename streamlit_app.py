# streamlit_app.py
import streamlit as st
import requests

# 1. PLACE THE API URL HERE AT THE TOP
API_URL = "https://stroke-risk-prediction-ml-api.onrender.com/predict"
# Set page configuration with a wide dashboard layout
st.set_page_config(page_title="Stroke Risk Analytics Platform", layout="wide")

# The direct, high-resolution source URL for your selected brain stroke vector
IMAGE_URL = "https://static.vecteezy.com/system/resources/previews/048/205/207/non_2x/a-illustration-of-human-brain-stroke-highlighting-medical-details-hemorrhage-and-pain-points-for-health-checks-in-a-flat-cartoon-background-vector.jpg"

# Custom CSS injection with a darker semi-transparent gradient tint
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Lora:ital,wght@0,500;1,400&display=swap');
    
    .stApp {{
        background-image: linear-gradient(rgba(10, 25, 30, 0.88), rgba(16, 37, 48, 0.88)), url("{IMAGE_URL}");
        background-size: cover;
        background-position: center center;
        background-attachment: fixed;
    }}
    
    .main-title {{
        font-family: 'Lora', serif;
        font-size: 44px;
        color: #00f2fe;
        font-weight: 700;
        margin-bottom: 2px;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.7);
    }}
    
    .sub-text {{
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        color: #ffffff;
        margin-bottom: 35px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.6);
    }}
    
    .metric-card {{
        background-color: rgba(12, 28, 36, 0.82);
        backdrop-filter: blur(12px);
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #00f2fe;
        margin-bottom: 20px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.5);
    }}
    
    .section-header {{
        font-family: 'Inter', sans-serif;
        font-size: 22px;
        color: #ffffff;
        font-weight: 600;
        margin-bottom: 15px;
    }}
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<div class="main-title">👑 NeuroVascular Risk Analytics</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Clinical predictive intelligence interface for real-time patient stroke probability metrics.</div>', unsafe_allow_html=True)

# Split the UI into two styled columns
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown('<div class="metric-card"><div class="section-header">📋 Vital Signs & Clinical Data</div>', unsafe_allow_html=True)
    age = st.slider("Patient Age (Years)", 0.0, 120.0, 45.0)
    avg_glucose_level = st.slider("Average Glucose Level (mg/dL)", 30.0, 300.0, 105.0)
    bmi = st.slider("Body Mass Index (BMI)", 10.0, 70.0, 24.5)
    
    hypertension = st.selectbox("History of Hypertension?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    heart_disease = st.selectbox("History of Heart Disease?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card"><div class="section-header">🧬 Demographics & Patient History</div>', unsafe_allow_html=True)
    gender = st.radio("Biological Gender", ["Female", "Male"], horizontal=True)
    married = st.radio("Ever Married?", ["No", "Yes"], horizontal=True)
    residence = st.radio("Residence Environment", ["Rural", "Urban"], horizontal=True)
    
    work = st.selectbox("Occupational Classification", ["Private", "Self-employed", "Govt_job", "children", "Never_worked"])
    smoking = st.selectbox("Tobacco Smoking History", ["never_smoked", "formerly_smoked", "smokes", "Unknown"])
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Centered action button
left_spacer, center_button, right_spacer = st.columns([1, 2, 1])
with center_button:
    calculate = st.button("📊 Execute Diagnostics Pipeline", use_container_width=True)

if calculate:
    payload = {
        "age": age, "hypertension": hypertension, "heart_disease": heart_disease,
        "avg_glucose_level": avg_glucose_level, "bmi": bmi,
        "gender_Male": 1 if gender == "Male" else 0,
        "ever_married_Yes": 1 if married == "Yes" else 0,
        "work_type_Private": 1 if work == "Private" else 0,
        "work_type_Self_employed": 1 if work == "Self-employed" else 0,
        "work_type_Govt_job": 1 if work == "Govt_job" else 0,
        "work_type_children": 1 if work == "children" else 0,
        "Residence_type_Urban": 1 if residence == "Urban" else 0,
        "smoking_status_formerly_smoked": 1 if smoking == "formerly_smoked" else 0,
        "smoking_status_never_smoked": 1 if smoking == "never_smoked" else 0,
        "smoking_status_smokes": 1 if smoking == "smokes" else 0
    }

    try:
        # 2. SWAPPED OUT THE LOCAL URL FOR THE CLOUD API_URL VARIABLE
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            res = response.json()
            prob = res["stroke_probability"] * 100
            
            st.markdown(f"### 📈 Diagnostics Assessment Output: **{res['risk_level']}**")
            if res["risk_level"] == "High Risk":
                st.error(f"Calculated Probability Score: {prob:.2f}% — Immediate neurological screening and preventative protocols are highly recommended.")
            else:
                st.success(f"Calculated Probability Score: {prob:.2f}% — Patient clinical indicators fall within typical baseline bounds.")
        else:
            st.error(f"❌ Backend Communication Error (Status {response.status_code})")
    except Exception as e:
        st.error(f"🔌 Connection Timeout: Ensure your FastAPI backend server is live. Details: {str(e)}")