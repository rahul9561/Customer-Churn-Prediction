Customer Churn Prediction Project
Overview
This project implements a customer churn prediction system for a telecom dataset (churn_data.csv). It features a Random Forest Classifier trained with scikit-learn, logged with MLflow, and served via a FastAPI backend. A React frontend (ChurnForm) allows users to input customer data for predictions. Logging is implemented to track training and API operations, with logs saved to logs/churn.log.
Project Structure
churn_project/
├── data/                      # Dataset
│   └── churnData.csv         # Telecom customer churn data
├── models/                    # Trained machine learning model
│   └── churn_model.pkl        # Saved Random Forest model
├── app/                       # FastAPI application
│   ├── __init__.py
│   ├── main.py                # FastAPI app with /v1/predict endpoint
│   ├── schemas.py             # Pydantic schemas for API requests/responses
│   ├── logger.py 
│   └── utils.py               # Model loading and prediction utilities
├── logs/                      # Log files
│   └── app.log              # Logs for training and API operations
├── train_model.py             # Script for model training and MLflow logging
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration for deployment
├── .gitignore                 # Git ignore file
├── README.md                  # Project documentation (this file)

Dataset
The churn_data.csv contains telecom customer data with 29 features and a churn target (0 = no churn, 1 = churn). Key features include:

Demographic: age, income, address, ed (education), employ (years employed).
Service Usage: tenure, longmon (long-distance minutes), tollmon, equipmon, cardmon, wiremon, longten, tollten, cardten.
Binary Features: equip, callcard, wireless, voice, pager, internet, callwait, confer, ebill.
Derived Features: loglong (log of long-distance minutes), logtoll, lninc (log of income).
Categorical: custcat (customer category, encoded as 1–4: Basic, Plus, E-Service, Total).

Prerequisites

Python 3.8+
Node.js (for React frontend, if used separately)
Docker (optional, for containerized deployment)
MLflow (for experiment tracking)
FastAPI server running locally or deployed

Installation

Clone the Repository:
git clone <repository-url>
cd churn_project


Set Up Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Prepare Dataset:

Ensure churn_data.csv is in the data/ directory with 29 features and a churn column.


Set Up Logging:

Create the logs/ directory to store churn.log:mkdir logs




Set Up MLflow (Optional):

Start an MLflow server:mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns


Access the MLflow UI at http://localhost:5000.



Usage
1. Train the Model
Run the training script to train the Random Forest Classifier:
python train_model.py


Output:
Model saved to models/churn_model.pkl.
Training logs (e.g., data loading, accuracy) written to logs/churn.log.
Metrics (accuracy, F1 score) and model logged to MLflow.



2. Run the FastAPI Server
Start the FastAPI server for predictions:
uvicorn app.main:app --host 127.0.0.1 --port 8000


Endpoint: POST /v1/predict
Input: JSON with 29 features (e.g., {"tenure": 12, "age": 34, ...}).
Output: {"churn": 0 or 1, "probability": float}.


Logs: API requests and predictions logged to logs/churn.log.

3. Use the React Frontend
The React frontend (ChurnForm) is a separate component for user input:

Set up a React project with react-hook-form, axios, and tailwindcss.
Add the ChurnForm component (provided separately) to your app.
Ensure the FastAPI server is running at http://127.0.0.1:8000.
Use the form to input customer data and view churn predictions.

4. Docker Deployment (Optional)
Build and run the project with Docker:
docker build -t churn_project .
docker run -p 8000:8000 churn_project


Access the API at http://127.0.0.1:8000.

Logging

File: logs/churn.log
Format: %(asctime)s - %(levelname)s - %(message)s
Content: Logs training steps (e.g., "Loaded dataset with 1000 rows", "Model Accuracy: 0.8500") and API operations (e.g., "Prediction: churn=0, probability=0.75").
Usage: Check logs/churn.log for debugging or monitoring.

API Details

Endpoint: POST /v1/predict
Request Body:{
  "tenure": 12,
  "age": 34,
  "income": 50000,
  "custcat": 1,
  "internet": 1,
  ...
  "lninc": 10.82
}


Response:{
  "churn": 0,
  "probability": 0.75
}


Note: The API expects all 29 features. Use default values (e.g., 0) for optional fields in the frontend.

Notes

Reducing Inputs: The React form has 29 fields, which may be overwhelming. Use feature importance (model.feature_importances_ in train_model.py) to select key features (e.g., tenure, age, custcat) and reduce form inputs.
Derived Features: Fields like lninc, loglong, logtoll are log-transformed. The frontend or API can compute these to simplify user input.
Frontend: The ChurnForm component is optimized for usability with a multi-step form and validation (see separate implementation).

Contributing

Fork the repository.
Create a feature branch (git checkout -b feature-name).
Commit changes (git commit -m "Add feature").
Push to the branch (git push origin feature-name).
Open a pull request.

License
MIT License