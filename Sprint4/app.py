from flask import Flask, request, jsonify
import joblib

#CREATE APP FIRST
app = Flask(__name__)

#  LOAD MODEL
model = joblib.load("intern_performance_model.pkl")

#  HOME ROUTE
@app.route('/')
def home():
    return "API is running successfully"

#  PREDICT ROUTE
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No input data provided"}), 400

        required_fields = [
            "completion_time",
            "feedback_rating",
            "attendance",
            "work_efficiency",
            "engagement_score",
            "productivity",
            "feedback_impact"
        ]

        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        try:
            features = [
                float(data["completion_time"]),
                float(data["feedback_rating"]),
                float(data["attendance"]),
                float(data["work_efficiency"]),
                float(data["engagement_score"]),
                float(data["productivity"]),
                float(data["feedback_impact"])
            ]
        except:
            return jsonify({"error": "Invalid input type"}), 400

        prediction = model.predict([features])[0]

        if prediction < 55:
            category = "Poor"
        elif prediction < 65:
            category = "Average"
        elif prediction < 75:
            category = "Good"
        else:
            category = "Excellent"

        return jsonify({
            "prediction": round(prediction, 2),
            "performance": category
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# RUN APP
if __name__ == '__main__':
    app.run(debug=True)