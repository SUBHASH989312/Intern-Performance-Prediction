from flask import Flask
import joblib

app = Flask(__name__)

# Load model using joblib
model = joblib.load("intern_performance_model.pkl")

@app.route('/')
def home():
    return "ML API is running successfully"

if __name__ == "__main__":
    app.run(debug=True)