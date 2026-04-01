import joblib
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")

# Load model
model = joblib.load("../Sprint4/intern_performance_model.pkl")

# Sample test data (same structure)
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

# Assume ACTUAL values (example ground truth)
actual_values = [50, 60, 72, 95]

df = pd.DataFrame(test_data, columns=columns)

# Predictions
predictions = model.predict(df)

# Error calculation
errors = np.abs(np.array(actual_values) - predictions)

# Output
for i in range(len(test_data)):
    print(f"\nInput: {test_data[i]}")
    print(f"Actual: {actual_values[i]}")
    print(f"Predicted: {predictions[i]:.2f}")
    print(f"Error: {errors[i]:.2f}")

# Average Error
print("\nAverage Error:", np.mean(errors))