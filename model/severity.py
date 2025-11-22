from model.symptoms_list import symptoms

# default weight = 1 for all symptoms
severity_weights =  {'itching':1, 'skin_rash':2, 'nodal_skin_eruptions':2, 'continuous_sneezing':1,
'shivering':2, 'chills':2, 'joint_pain':2, 'stomach_pain':2, 'acidity':1, 'ulcers_on_tongue':2,
'muscle_wasting':3, 'vomiting':2, 'burning_micturition':3, 'spotting_ urination':3, 'fatigue':1,
'weight_gain':1, 'anxiety':1, 'cold_hands_and_feets':1, 'mood_swings':1, 'weight_loss':1,
'restlessness':1, 'lethargy':1, 'patches_in_throat':2, 'irregular_sugar_level':3, 'cough':2,
'high_fever':5, 'sunken_eyes':2, 'breathlessness':5, 'sweating':2, 'dehydration':3,
'indigestion':1, 'headache':1, 'yellowish_skin':3, 'dark_urine':3, 'nausea':1,
'loss_of_appetite':1, 'pain_behind_the_eyes':2, 'back_pain':2, 'constipation':1, 'abdominal_pain':2,
'diarrhoea':2, 'mild_fever':2, 'yellow_urine':2, 'yellowing_of_eyes':3, 'acute_liver_failure':5,
'fluid_overload':4, 'swelling_of_stomach':3, 'swelled_lymph_nodes':3, 'malaise':1,
'blurred_and_distorted_vision':2, 'phlegm':1, 'throat_irritation':1, 'redness_of_eyes':1,
'sinus_pressure':1, 'runny_nose':1, 'congestion':1, 'chest_pain':5, 'weakness_in_limbs':2,
'fast_heart_rate':3, 'pain_during_bowel_movements':2, 'pain_in_anal_region':2, 'bloody_stool':4,
'irritation_in_anus':2, 'neck_pain':2, 'dizziness':2, 'cramps':1, 'bruising':2, 'obesity':1,
'swollen_legs':2, 'swollen_blood_vessels':3, 'puffy_face_and_eyes':2, 'enlarged_thyroid':3,
'brittle_nails':1, 'swollen_extremeties':2, 'excessive_hunger':2, 'extra_marital_contacts':1,
'drying_and_tingling_lips':1, 'slurred_speech':4, 'knee_pain':2, 'hip_joint_pain':2, 'muscle_weakness':3,
'stiff_neck':4, 'swelling_joints':2, 'movement_stiffness':2, 'spinning_movements':3,
'loss_of_balance':3, 'unsteadiness':2, 'weakness_of_one_body_side':4, 'loss_of_smell':2,
'bladder_discomfort':2, 'foul_smell_of urine':2, 'continuous_feel_of_urine':2, 'passage_of_gases':1,
'internal_itching':1, 'toxic_look_(typhos)':5, 'depression':1, 'irritability':1, 'muscle_pain':2,
'altered_sensorium':5, 'red_spots_over_body':2, 'belly_pain':2, 'abnormal_menstruation':2,
'dischromic _patches':2, 'watering_from_eyes':1, 'increased_appetite':1, 'polyuria':2,
'family_history':1, 'mucoid_sputum':2, 'rusty_sputum':2, 'lack_of_concentration':1,
'visual_disturbances':2, 'receiving_blood_transfusion':2, 'receiving_unsterile_injections':2,
'coma':5, 'stomach_bleeding':4, 'distention_of_abdomen':3, 'history_of_alcohol_consumption':2,
'fluid_overload.1':4, 'blood_in_sputum':4, 'prominent_veins_on_calf':2, 'palpitations':3,
'painful_walking':2, 'pus_filled_pimples':2, 'blackheads':1, 'scurring':1, 'skin_peeling':1,
'silver_like_dusting':1, 'small_dents_in_nails':1, 'inflammatory_nails':2, 'blister':2,
'red_sore_around_nose':2, 'yellow_crust_ooze':2}

def calculate_severity(selected_symptoms):
    score = sum(severity_weights[s] for s in selected_symptoms)

    if score < 5:
        return "Mild", score
    elif score < 12:
        return "Moderate", score
    else:
        return "Severe", score
