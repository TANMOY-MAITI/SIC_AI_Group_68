import joblib
import numpy as np
from model.symptoms_list import symptoms

# Load trained model and PCA
model = joblib.load("model/disease_rf_model.pkl")
pca = joblib.load("model/pca.pkl")  # load the same PCA used in training

def predict_disease(selected_symptoms):
    # Create binary input vector
    input_vector = np.zeros(len(symptoms))
    for s in selected_symptoms:
        if s in symptoms:
            input_vector[symptoms.index(s)] = 1

    # Transform using PCA
    input_vector_pca = pca.transform([input_vector])

    # Make prediction
    prediction = model.predict(input_vector_pca)[0]
    confidence = max(model.predict_proba(input_vector_pca)[0]) * 100

    return prediction, round(confidence, 2)
