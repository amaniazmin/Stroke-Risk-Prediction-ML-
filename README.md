# 🧠 Stroke Risk Analytics Platform

A production-grade Machine Learning system that predicts stroke probability in real-time, served via FastAPI REST API with a live Streamlit dashboard and an automated CI/CD pipeline.

### 🔗 Live Links

| Resource | Link |
| :--- | :--- |
| **🌐 Live Dashboard** | [Click Here](https://6sa3ffvjn622xtcuzutpp2.streamlit.app/) |
| **📖 API Documentation** | [Click Here](https://stroke-risk-prediction-ml-api.onrender.com/docs) |
| **📊 GitHub Actions** | [Click Here](https://github.com/amaniazmin/Stroke-Risk-Prediction-ML-/actions) |

---

### 🎯 Project Overview

Built an end-to-end medical diagnostic system trained on the **Stroke Prediction Dataset** (5,110 patient records). The system processes 11 clinical and lifestyle features—including BMI, glucose levels, and hypertension—to provide an immediate stroke risk assessment, facilitating early medical intervention.

### 📊 Model Performance

| Metric | Score |
| :--- | :--- |
| **Model** | XGBoost / Random Forest |
| **Primary Goal** | High-Sensitivity Risk Classification |
| **Robustness** | Ensemble-based over-fitting mitigation |

---

### 🏗️ System Architecture



* **User Input:** Clinical vitals entered via dashboard.
* **API Layer:** FastAPI processes input and validates via Pydantic.
* **Inference Engine:** Scikit-learn/XGBoost models predict risk level.
* **Outcome:** Real-time probability percentage displayed to user.

---

### 🛠️ Tech Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **ML Models** | scikit-learn, XGBoost | Classification & Ensemble tuning |
| **API Backend** | FastAPI + Uvicorn | High-performance REST API |
| **Dashboard** | Streamlit | Medical-themed UI |
| **Testing** | pytest | Automated test suite |
| **CI/CD** | GitHub Actions | Automated build & test pipeline |
| **Deployment** | Render + Streamlit Cloud | Global cloud hosting |