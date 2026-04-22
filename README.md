# Stroke Risk Prediction using Machine Learning
### Tools: Python, Scikit-Learn, XGBoost | Models: Random Forest, Decision Tree, XGBoost

## Project Overview
This project aims to predict the likelihood of a patient experiencing a stroke based on 11 clinical and lifestyle features, including BMI, glucose levels, and hypertension. The goal was to build a highly accurate classification model that can assist in early medical intervention.

## Dataset
The analysis uses the **Stroke Prediction Dataset** from Kaggle, containing 5,110 patient records.
- **Features**: Age, hypertension, heart disease, average glucose level, BMI, smoking status, and more.
- **Target**: Stroke occurrence (Binary: Yes/No).

## Machine Learning Workflow
1. **Data Cleaning**: Handled missing values (especially in BMI) and performed encoding for categorical variables.
2. **Exploratory Data Analysis (EDA)**: Visualized correlations between age, glucose levels, and stroke risk.
3. **Model Implementation**: Built and tuned three different classification algorithms:
   - **Decision Tree**: For baseline classification.
   - **Random Forest**: An ensemble method to reduce overfitting.
   - **XGBoost**: For high-performance gradient boosting.
4. **Performance Evaluation**: Compared models using Accuracy, Precision, Recall, and F1-Score.

## Key Results
After evaluating the models, the following performance was observed:
* **XGBoost** and **Random Forest** consistently outperformed the single Decision Tree, providing more robust predictions for high-risk patients.
