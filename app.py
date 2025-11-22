import streamlit as st
from model.symptoms_list import symptoms
from model.predictor import predict_disease
from model.severity import calculate_severity

st.set_page_config(page_title="Disease Prediction App")

# ---------------- Home Page ----------------
st.title("🩺 Disease Diagnosis from Symptoms")
st.write("""
This ML-powered app predicts possible diseases based on symptoms.
Select symptoms → Get predicted disease, confidence & severity level.
""")

st.subheader("Select your symptoms")
selected = st.multiselect("Choose symptoms you are experiencing:", symptoms)

if st.button("Predict Disease"):
    if len(selected) == 0:
        st.error("Please select at least one symptom.")
    else:
        # Predict disease
        disease, confidence = predict_disease(selected)

        # Severity
        level, score = calculate_severity(selected)

        st.success(f"### 🧠 Predicted Disease: **{disease}**")
        st.info(f"### 🔢 Confidence Score: **{confidence}%**")
        st.warning(f"### ❤️ Severity Level: **{level} (Score: {score})**")

        # Recommendations
        if level == "Mild":
            st.write("💡 *Home remedies should be fine.*")
        elif level == "Moderate":
            st.write("⚠️ *Consult a doctor soon.*")
        else:
            st.write("🚨 *Immediate medical attention recommended.*")
