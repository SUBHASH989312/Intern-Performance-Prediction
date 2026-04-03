from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load("../Sprint5/intern_performance_model_v2.pkl")

@app.route('/')
def home():
    return "API is running!"

@app.route('/predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'GET':
        data = request.args

        input_data = [[
            float(data.get('Completion_Time', 5)),
            float(data.get('Feedback_Rating', 4)),
            float(data.get('Attendance', 80)),
            float(data.get('Work_Efficiency', 0.06)),
            float(data.get('Engagement_Score', 320)),
            float(data.get('Productivity', 20)),
            float(data.get('Feedback_Impact', 16))
        ]]
    else:
        data = request.get_json()

        input_data = [[
            data['Completion_Time'],
            data['Feedback_Rating'],
            data['Attendance'],
            data['Work_Efficiency'],
            data['Engagement_Score'],
            data['Productivity'],
            data['Feedback_Impact']
        ]]

    prediction = model.predict(input_data)[0]

    if prediction < 55:
        category = "Poor"
    elif prediction < 65:
        category = "Average"
    elif prediction < 75:
        category = "Good"
    else:
        category = "Excellent"

    return jsonify({
        "prediction_score": round(prediction, 2),
        "performance_category": category
    })


import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))