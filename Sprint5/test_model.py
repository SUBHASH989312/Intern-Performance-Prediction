import joblib
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

# ✅ Correct path
model = joblib.load("../Sprint4/intern_performance_model.pkl")

columns = [
    "Completion_Time",
    "Feedback_Rating",
    "Attendance",
    "Work_Efficiency",
    "Engagement_Score",
    "Productivity",
    "Feedback_Impact"
]

test_data = [
    [9.0, 2.0, 40, 0.22, 80, 18.0, 4.0],
    [5.0, 3.0, 60, 0.10, 180, 18.0, 9.0],
    [5.5, 4.5, 55, 0.037, 320, 12.0, 16.0],
    [1.5, 5.0, 100, 0.015, 500, 7.5, 25.0]
]

df = pd.DataFrame(test_data, columns=columns)

predictions = model.predict(df)

for i, data in enumerate(test_data):
    prediction = predictions[i]

    if prediction < 55:
        category = "Poor"
    elif prediction < 65:
        category = "Average"
    elif prediction < 75:
        category = "Good"
    else:
        category = "Excellent"

    # ✅ Indented inside the loop
    print(f"Input: {data} -> Prediction: {prediction:.2f} -> Category: {category}")