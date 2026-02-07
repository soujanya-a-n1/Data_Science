import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import joblib
import os

# Load dataset
df = pd.read_csv("data/housing.csv")

print("Dataset Shape:", df.shape)
print("Columns:", df.columns)

# Select features and target
X = df[['area', 'bedrooms', 'bathrooms']]
y = df['price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = r2_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.pkl")

print("Model saved successfully at model/model.pkl")
