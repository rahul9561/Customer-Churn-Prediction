import pandas as pd
import numpy as np
import joblib
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import os
from app.logger import logger  # custom logger

# Ensure model directory exists
os.makedirs("models", exist_ok=True)

# Load dataset
logger.info("Loading dataset...")
data = pd.read_csv("data/churnData.csv")

# Features & Target
X = data.drop("churn", axis=1)
y = data["churn"]

logger.info(f"Dataset loaded with shape {data.shape}. Splitting train/test...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize model
model = RandomForestClassifier(n_estimators=100, random_state=42)

logger.info("Starting model training...")
with mlflow.start_run():
    # Train
    model.fit(X_train, y_train)
    logger.info("Model training completed.")

    # Predictions
    preds = model.predict(X_test)

    # Metrics
    acc = accuracy_score(y_test, preds)
    f1 = f1_score(y_test, preds)

    logger.info(f"Accuracy: {acc:.4f}, F1 Score: {f1:.4f}")

    # Log metrics
    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("f1_score", f1)

    # Log model with signature
    input_example = X_train.iloc[:1]
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model",
        input_example=input_example
    )

# Save model locally
joblib.dump(model, "models/churn_model.pkl")
logger.info("Model saved at models/churn_model.pkl")

print("✅ Model trained & saved as models/churn_model.pkl")
