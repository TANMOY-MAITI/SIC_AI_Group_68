import joblib
import numpy as np
from model.symptoms_list import symptoms

model = joblib.load("model/disease_rf_model.pkl")

def predict_disease(selected_symptoms):
    input_vector = np.zeros(len(symptoms))

    for s in selected_symptoms:
        input_vector[symptoms.index(s)] = 1

    prediction = model.predict([input_vector])[0]
    confidence = max(model.predict_proba([input_vector])[0]) * 100

    return prediction, round(confidence, 2)
