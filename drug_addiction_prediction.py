from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = float(request.form['age'])
        gender = 0 if request.form['gender'] == 'Male' else 1
        academic_performance = float(request.form['academic_performance'])
        attendance = float(request.form['attendance'])
        social_influence = float(request.form['social_influence'])
        behavioral_issues = int(request.form['behavioral_issues'])
        family_background = int(request.form['family_background'])
        stress_level = float(request.form['stress_level'])

        features = np.array([[age, gender, academic_performance, attendance, social_influence, behavioral_issues, family_background, stress_level]])
        features_scaled = scaler.transform(features)

        prediction = model.predict(features_scaled)

        result = 'Based on the prediction outcome, it appears the individual is categorized as an addict.' if prediction[0] == 1 else 'Based on the prediction outcome, it appears the individual is categorized as not an addict.'
        
    except Exception as e:
        result = f"Error: {e}"

    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
