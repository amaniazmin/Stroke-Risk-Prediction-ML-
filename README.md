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
