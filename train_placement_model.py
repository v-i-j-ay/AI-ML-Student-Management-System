import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import joblib

# Load dataset
data = pd.read_csv("placement_dataset.csv")

# Features (Input)
X = data[
    [
        "marks",
        "attendance",
        "projects",
        "communication",
        "internships",
        "cgpa"
    ]
]

# Target (Output)
y = data["placement_status"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Model
model = RandomForestClassifier(random_state=42)

# Train Model
model.fit(X_train, y_train)

# Prediction
prediction = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, prediction)

print("=" * 50)
print("Placement Prediction Model")
print("=" * 50)
print(f"Accuracy : {accuracy * 100:.2f}%")

# Save Model
joblib.dump(model, "placement_model.pkl")

print("\nModel Saved Successfully!")