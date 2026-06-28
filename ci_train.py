# ci_train.py
import os
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

def train_real_model():
    print("🤖 Loading raw dataset...")
    csv_path = "stroke_data.csv"
    
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"❌ Could not find {csv_path}!")
        
    df = pd.read_csv(csv_path)
    
    # 1. Convert categorical text columns into numeric dummy/one-hot flags
    df_encoded = pd.get_dummies(df, columns=['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status'])
    
    # 2. Define the exact 15 features your FastAPI schema expects
    feature_cols = [
        'age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi',
        'gender_Male', 'ever_married_Yes', 'work_type_Private', 
        'work_type_Self_employed', 'work_type_Govt_job', 'work_type_children',
        'Residence_type_Urban', 'smoking_status_formerly_smoked', 
        'smoking_status_never_smoked', 'smoking_status_smokes'
    ]
    
    # 3. Create missing dummy columns with 0s if they don't appear in this dataset slice
    for col in feature_cols:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
            
    X = df_encoded[feature_cols]
    y = df_encoded['stroke']
    
    print("📊 Fitting scaler and Random Forest model on encoded columns...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_scaled, y)
    
    os.makedirs("models", exist_ok=True)
    
    print("💾 Saving updated structural artifacts to /models directory...")
    with open("models/stroke_model.pkl", "wb") as f:
        pickle.dump(model, f)
    with open("models/scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)
    print("✅ Success! Your model parameters are aligned with your dataset columns.")

if __name__ == "__main__":
    train_real_model()