import pandas as pd
import numpy as np
import joblib
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import os
from app.logger import logger  # your custom logger

# --------------------------
# Config
# --------------------------
os.makedirs("models", exist_ok=True)
DATA_PATH = "data/ChurnData.csv"
EXPERIMENT_NAME = "Churn_Prediction"

# Set MLflow experiment
mlflow.set_experiment(EXPERIMENT_NAME)

# --------------------------
# Load dataset
# --------------------------
logger.info("Loading dataset...")
data = pd.read_csv(DATA_PATH)

X = data.drop("churn", axis=1)
y = data["churn"]

logger.info(f"Dataset loaded with shape {data.shape}. Splitting train/test...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --------------------------
# Initialize model
# --------------------------
n_estimators = 100
random_state = 42
model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)

# --------------------------
# Train & log with MLflow
# --------------------------
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

    # Log params & metrics
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("random_state", random_state)
    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("f1_score", f1)

    # Log model with input example
    input_example = X_train.iloc[:1]
    mlflow.sklearn.log_model(
        sk_model=model,
        name="churn_model",
        input_example=input_example
    )

# --------------------------
# Save model locally
# --------------------------
joblib.dump(model, "models/churn_model.pkl")
logger.info("Model saved at models/churn_model.pkl")

print("✅ Model trained & saved as models/churn_model.pkl")
