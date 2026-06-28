<<<<<<< HEAD
🧠 Stroke Risk Analytics PlatformA production-grade Machine Learning system that predicts stroke probability in real-time, served via FastAPI REST API with a live Streamlit dashboard and an automated CI/CD pipeline.🔗 Live LinksResourceLink🌐 Live DashboardClick Here📖 API DocumentationClick Here📊 GitHub ActionsClick Here🎯 Project OverviewBuilt an end-to-end medical diagnostic system trained on the Stroke Prediction Dataset (5,110 patient records). The system processes 11 clinical and lifestyle features—including BMI, glucose levels, and hypertension—to provide an immediate stroke risk assessment, facilitating early medical intervention.📊 Model PerformanceMetricScoreModelXGBoost / Random ForestPrimary GoalHigh-Sensitivity Risk ClassificationRobustnessEnsemble-based over-fitting mitigation🏗️ System ArchitectureUser Input: Clinical vitals entered via dashboard.API Layer: FastAPI processes input and validates via Pydantic.Inference Engine: Scikit-learn/XGBoost models predict risk level.Outcome: Real-time probability percentage displayed to user.🛠️ Tech StackLayerTechnologyPurposeML Modelsscikit-learn, XGBoostClassification & Ensemble tuningAPI BackendFastAPI + UvicornHigh-performance REST APIDashboardStreamlitMedical-themed UITestingpytestAutomated test suiteCI/CDGitHub ActionsAutomated build & test pipelineDeploymentRender + Streamlit CloudGlobal cloud hosting🚀 Run LocallyClone the repository:Bashgit clone https://github.com/amaniazmin/Stroke-Risk-Prediction-ML-.git
cd Stroke-Risk-Prediction-ML-
Setup virtual environment:Bashpython -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
Install dependencies:Bashpip install -r requirements.txt
Start FastAPI backend:Bashuvicorn app.main:app --reload
Start Streamlit dashboard (new terminal):Bashstreamlit run streamlit_app.py
📁 Project StructurePlaintextStroke-Risk-Prediction-ML-/
├── app/
│   ├── main.py          # FastAPI routes & prediction logic
│   └── schemas.py       # Pydantic data validation
├── models/
│   ├── stroke_model.pkl # Trained predictive model
│   └── scaler.pkl       # Feature standardization
├── tests/
│   └── test_api.py      # Automated API verification
├── .github/workflows/
│   └── build-and-test.yml # CI/CD automation
├── streamlit_app.py     # Live interactive dashboard
└── requirements.txt     # Dependency management
👩‍💻 AuthorAmani AzminGitHub: @amaniazmin📄 LicenseMIT License
=======
# 🧠 Stroke Risk Analytics Platform

A production-grade Machine Learning system that predicts stroke probability in real-time, served via FastAPI REST API with a live Streamlit dashboard and an automated CI/CD pipeline.

### 🔗 Live Links

| Resource | Link |
| :--- | :--- |
| **🌐 Live Dashboard** | [Click Here](YOUR_STREAMLIT_URL_HERE) |
| **📖 API Documentation** | [Click Here](https://stroke-risk-prediction-ml-api.onrender.com/docs) |
| **📊 GitHub Actions** | [Click Here](https://github.com/amaniazmin/Stroke-Risk-Prediction-ML-/actions) |

---

### 🎯 Project Overview

Built an end-to-end medical diagnostic system trained on the **Stroke Prediction Dataset**. The system processes 11 clinical and lifestyle features to provide immediate stroke risk assessment.

### 📊 Model Performance

| Metric | Score |
| :--- | :--- |
| **Model** | XGBoost / Random Forest |
| **Focus** | High-Sensitivity Risk Classification |

---

### 🏗️ System Architecture

* **User Input:** Clinical vitals entered via dashboard.
* **API Layer:** FastAPI processes input and validates via Pydantic.
* **Inference Engine:** Scikit-learn models predict risk level.
* **Outcome:** Real-time probability percentage displayed to user.

---

### 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **ML Models** | scikit-learn, XGBoost |
| **API Backend** | FastAPI + Uvicorn |
| **Dashboard** | Streamlit |
| **CI/CD** | GitHub Actions |
| **Deployment** | Render + Streamlit Cloud |

---

### 🚀 Run Locally

1. **Clone:** `git clone https://github.com/amaniazmin/Stroke-Risk-Prediction-ML-.git`
2. **Install:** `pip install -r requirements.txt`
3. **Backend:** `uvicorn app.main:app --reload`
4. **Frontend:** `streamlit run streamlit_app.py`

---

### 📁 Project Structure

```text
Stroke-Risk-Prediction-ML-/
├── app/             # FastAPI routes & logic
├── models/          # Trained .pkl files
├── tests/           # Automated tests
├── .github/         # CI/CD pipeline
└── streamlit_app.py # Dashboard
>>>>>>> 7b675bd (Docs: Update README with professional formatting)
