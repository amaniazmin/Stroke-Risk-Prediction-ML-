from pydantic import BaseModel, Field

class StrokeInput(BaseModel):
    age: float = Field(..., ge=0, le=120)
    hypertension: int = Field(..., ge=0, le=1)
    heart_disease: int = Field(..., ge=0, le=1)
    avg_glucose_level: float = Field(..., ge=30.0, le=300.0)
    bmi: float = Field(..., ge=10.0, le=70.0)
    gender_Male: int = Field(..., ge=0, le=1)
    ever_married_Yes: int = Field(..., ge=0, le=1)
    work_type_Private: int = Field(..., ge=0, le=1)
    work_type_Self_employed: int = Field(..., ge=0, le=1)
    work_type_Govt_job: int = Field(..., ge=0, le=1)
    work_type_children: int = Field(..., ge=0, le=1)
    Residence_type_Urban: int = Field(..., ge=0, le=1)
    smoking_status_formerly_smoked: int = Field(..., ge=0, le=1)
    smoking_status_never_smoked: int = Field(..., ge=0, le=1)
    smoking_status_smokes: int = Field(..., ge=0, le=1)

class StrokePredictionResponse(BaseModel):
    stroke_probability: float
    stroke_risk_prediction: int
    risk_level: str
