import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load Dataset
data = pd.read_csv("performance_dataset.csv")

# Input Features
X = data[[
    "marks",
    "attendance",
    "projects",
    "internships",
    "cgpa"
]]

# Target Value
y = data["next_sem_marks"]

# Train Model
model = LinearRegression()
model.fit(X, y)

# Save Model
joblib.dump(model, "performance_model.pkl")

print("Performance Prediction Model Trained Successfully!")
print("Model saved as performance_model.pkl")