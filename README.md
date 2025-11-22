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
