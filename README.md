# Disease Diagnosis from Patient Symptoms (SIC AI Project)

## Overview
This project predicts possible diseases based on patient-reported symptoms using a **Random Forest ML model**. It also calculates **severity levels** and gives **actionable suggestions** (Home care, Doctor needed, Emergency).

The project is built using **Python**, **Scikit-learn**, and **Streamlit** for the web interface.

---

## Folder Structure

SIC_AI_Group_68/
│
├── app.py # Streamlit main app
├── model/
│ ├── disease_rf_model.pkl
│ ├── severity.py # Severity scoring functions
│ ├── predictor.py # Disease prediction functions
│ └── symptoms_list.py # List of 132 symptoms
│
├── data/
│ ├── Testing.csv
│ └── Training.csv
│
├── notebooks/
│ └── Disease_diagnosis_from_patient_symptoms.ipynb
│
├── requirements.txt
└── README.md

---

## Features

- Predict disease from **132 possible symptoms → 41 diseases**  
- Calculate **severity score** and classify as: Mild / Moderate / Severe  
- Show **confidence score** for predictions  
- **Streamlit web app** with sidebar navigation: Home → Symptoms → Result  
- Optional disease info, prevention tips, and guidance  

---

## Installation

1. Clone the repo:

git clone https://github.com/TANMOY-MAITI/SIC_AI_Group_68.git
cd SIC_AI_Group_68

2. Install dependencies:

pip install -r requirements.txt
  
3. Run the Streamlit app:

streamlit run app.py

---

## Usage

1. Open the app in your browser.

2. Navigate to Symptoms Input and select all symptoms you are experiencing.

3. Go to Diagnosis Result to see:

. Predicted disease

. Confidence score

. Severity rating

. Suggested action

Note: This app is for educational purposes only. For medical advice, always consult a doctor.

---

# Basic information 


## Project description in short 

This project is a **machine learning-based disease diagnosis system** that predicts possible diseases based on patient symptoms. The system leverages a RandomForest model trained on historical symptom-disease data, with PCA for dimensionality reduction.

## How It Works

1. Users select their symptoms from a predefined list.
2. The symptoms are converted into a numerical input vector.
3. The input vector is transformed using PCA (65 principal components).
4. The RandomForest model predicts the most probable disease and confidence score.
5. Optionally, severity is calculated based on the selected symptoms.

## Main Functionality

* Interactive symptom selection through a Streamlit interface.
* Disease prediction with probability/confidence.
* Severity estimation.
* Modular structure for easy expansion and updates.

## Tech Stack

* Python 3.13
* Streamlit for web interface
* scikit-learn for ML models (RandomForest, PCA)
* NumPy & Pandas for data handling
* Joblib for saving/loading models

## Benefits

* Quick and easy preliminary diagnosis.
* Helps users understand potential diseases without immediate hospital visits.
* Provides confidence levels for transparency.

## Drawbacks

* Dependent on the quality and diversity of training data.
* PCA may reduce interpretability for some users.
* Cannot replace professional medical advice.

## Problem Statement

Many people face **delays in disease diagnosis** due to lack of quick access to doctors or awareness of symptoms. Misdiagnosis or late detection can lead to worsened health outcomes.

## Solution

A **digital diagnostic tool** that predicts possible diseases from reported symptoms, helping users make informed decisions and seek timely medical advice.

## Key Innovations

* Use of **PCA for dimensionality reduction** to handle high-dimensional symptom data.
* **RandomForestClassifier** for robust and accurate predictions.
* Streamlit-based **user-friendly interface** for interactive symptom selection.

## Algorithm and Workflow

1. **Data Preprocessing:** Clean, encode, and normalize symptom-disease data.
2. **PCA Transformation:** Reduce 132 symptoms to 65 components.
3. **Model Training:** Train RandomForestClassifier on PCA-transformed data.
4. **Prediction:** Transform user input using PCA → predict disease → calculate confidence.
5. **Output:** Display disease name, confidence score, and severity.

## Future Scope

* Integrate additional features like patient history and age.
* Expand dataset for rare diseases.
* Include multi-language support for wider accessibility.
* Incorporate more advanced algorithms like XGBoost or ensemble learning.
* Add explainability features to interpret predictions.

## Conclusion

This project provides a **fast, interactive, and data-driven approach to disease prediction**. It addresses the problem of delayed diagnosis and empowers users to make informed decisions while highlighting the importance of seeking professional medical advice.

