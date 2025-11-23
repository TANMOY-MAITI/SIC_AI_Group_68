from flask import Flask, render_template, request
import numpy as np
import traceback

app = Flask(__name__)

# Import your existing model code (as requested)
try:
    from model.predictor import predict_disease
    from model.severity import calculate_severity
    from model.symptoms_list import symptoms
except Exception as e:
    # Helpful error message if imports fail (edit paths/names if needed)
    msg = (
        "Failed to import from model/.\n"
        "Make sure model/predictor.py defines predict_disease,\n"
        "model/severity.py defines calculate_severity,\n"
        "and model/symptoms_list.py defines symptoms (list).\n\n"
        f"Original error: {e}\n{traceback.format_exc()}"
    )
    raise ImportError(msg)

@app.route("/", methods=["GET"])
def home():
    # Render form with the symptom names (list of strings)
    return render_template("index.html", symptoms=symptoms)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Build symptom vector in the same order as symptoms list.
        # We expect each input to be a checkbox (value '1' when present).
        symptom_vector = []
        for s in symptoms:
            # request.form.get returns None if unchecked; default to '0'
            val = request.form.get(s, "0")
            # convert to int (0/1) safely
            try:
                symptom_vector.append(int(val))
            except:
                # fallback if some inputs are "yes"/"no"
                symptom_vector.append(1 if str(val).lower() in ("1","true","yes","on") else 0)

        arr = np.array([symptom_vector])

        # Call your project functions (they should accept the vector)
        disease = predict_disease(arr)        # If your function expects list/ndarray it will work
        severity = calculate_severity(arr)   # same for severity

        # If the functions return arrays, extract first element
        if isinstance(disease, (list, tuple, np.ndarray)):
            disease = disease[0]
        if isinstance(severity, (list, tuple, np.ndarray)):
            severity = severity[0]

        return render_template("index.html",
                               symptoms=symptoms,
                               prediction=str(disease),
                               severity=str(severity),
                               input_count=len(symptom_vector))
    except Exception as e:
        # show error on page for quick debugging in local dev
        return render_template("index.html",
                               symptoms=symptoms,
                               error=str(e),
                               traceback=traceback.format_exc())

if __name__ == "__main__":
    # debug=True is handy locally; set to False in production
    app.run(host="127.0.0.1", port=5000, debug=True)
