import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "completion_time": 3.5,
    "feedback_rating": 4.4,
    "attendance": 98,
    "work_efficiency": 78,
    "engagement_score": 80,
    "productivity": 75,
    "feedback_impact": 70
}

response = requests.post(url, json=data)

print(response.json())