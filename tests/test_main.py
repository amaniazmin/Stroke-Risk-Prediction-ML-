import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    """Test that the API root endpoint returns a 200 OK health check status."""
    response = client.get("/")
    assert response.status_code == 200
    assert "status" in response.json()

def test_predict_stroke_risk_positive():
    """Test the prediction endpoint with mock high-risk patient metrics."""
    test_payload = {
        "age": 67.0,
        "hypertension": 0,
        "heart_disease": 1,
        "avg_glucose_level": 228.69,
        "bmi": 36.6,
        "gender_Male": 1,
        "ever_married_Yes": 1,
        "work_type_Govt_job": 0,
        "work_type_Private": 1,
        "work_type_Self_employed": 0,
        "work_type_children": 0,
        "Residence_type_Urban": 1,
        "smoking_status_formerly_smoked": 1,
        "smoking_status_never_smoked": 0,
        "smoking_status_smokes": 0
    }
    
    response = client.post("/predict", json=test_payload)
    assert response.status_code == 200
    
    response_data = response.json()
    # Key match alignment fix
    assert "stroke_probability" in response_data
    assert "risk_level" in response_data