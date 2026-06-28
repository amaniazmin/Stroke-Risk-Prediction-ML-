# app/main.py
import os
import pickle
import pandas as pd
from fastapi import FastAPI, HTTPException
from app.schemas import StrokeInput

app = FastAPI(title="Stroke Risk Prediction API")

MODEL_PATH = "models/stroke_model.pkl"
SCALER_PATH = "models/scaler.pkl"

# CRITICAL FIX: Properly load the pickle files without typos
if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    with open(SCALER_PATH, "rb") as f:
        scaler = pickle.load(f)
else:
    model = None
    scaler = None

FEATURE_NAMES = [
    'age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi',
    'gender_Male', 'ever_married_Yes', 'work_type_Private', 
    'work_type_Self_employed', 'work_type_Govt_job', 'work_type_children',
    'Residence_type_Urban', 'smoking_status_formerly_smoked', 
    'smoking_status_never_smoked', 'smoking_status_smokes'
]

@app.get("/")
def read_root():
    return {"status": "healthy", "message": "API is running smoothly."}

@app.post("/predict")
def predict_stroke(payload: StrokeInput):
    if model is None or scaler is None:
        raise HTTPException(status_code=503, detail="Machine learning model artifacts are missing or not trained.")
    
    try:
        input_data = payload.dict()
        row_values = [input_data[col] for col in FEATURE_NAMES]
        
        # Convert to DataFrame to retain valid feature names for the scaler
        features_df = pd.DataFrame([row_values], columns=FEATURE_NAMES)
        
        scaled_features = scaler.transform(features_df)
        probability = model.predict_proba(scaled_features)[0][1]
        
        risk_level = "High Risk" if probability >= 0.50 else "Low Risk"
        
        return {
            "stroke_probability": float(probability),
            "risk_level": risk_level
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Processing Error: {str(e)}")