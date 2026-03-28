#  Intern Performance Prediction API

##  Project Overview
This project predicts intern performance using a Machine Learning model deployed as a Flask API.  
It takes various performance-related inputs and returns a predicted score along with a performance category (Excellent, Good, Average).

---

##  Objective
The goal of this project is to:
- Analyze intern performance based on multiple factors  
- Build a machine learning model for prediction  
- Deploy the model as a live API  
- Make it accessible via a public URL  

---

##  Live API
🔗 https://intern-performance-prediction.onrender.com/predict
   u can use postman.
---

##  Input Features
The API accepts the following input features:

- completion_time (float)
- feedback_rating (float)
- attendance (int)
- work_efficiency (int)
- engagement_score (int)
- productivity (int)
- feedback_impact (int)

---

##  Sample Request
```json
{
  "completion_time": 3.5,
  "feedback_rating": 4.2,
  "attendance": 85,
  "work_efficiency": 78,
  "engagement_score": 80,
  "productivity": 75,
  "feedback_impact": 70
}

##  Sample Response
```json
{
  "prediction": 76.99,
  "performance": "Excellent"
}