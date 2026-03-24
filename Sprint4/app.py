from flask import Flask, request, jsonify
import joblib
import numpy as np

# ✅ Create app FIRST
app = Flask(__name__)

# Load model
model = joblib.load("intern_performance_model.pkl")

# Home route
@app.route('/')
def home():
    return "ML API is running successfully"

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)

        prediction = model.predict(features)[0]

        # Category logic
        if prediction < 55:
            category = "Poor"
        elif prediction < 65:
            category = "Average"
        elif prediction < 75:
            category = "Good"
        else:
            category = "Excellent"

        return jsonify({
            "prediction": float(prediction),
            "performance": category
        })

    except Exception as e:
        return jsonify({"error": str(e)})

# Run app
if __name__ == "__main__":
    app.run(debug=True)