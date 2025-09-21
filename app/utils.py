import joblib
import pandas as pd
from app.schemas import ChurnRequest

# Load saved model
model = joblib.load("models/churn_model.pkl")

FEATURE_COLUMNS = [
    "tenure","age","address","income","ed","employ","equip","callcard","wireless",
    "longmon","tollmon","equipmon","cardmon","wiremon","longten","tollten","cardten",
    "voice","pager","internet","callwait","confer","ebill","loglong","logtoll","lninc","custcat"
]

def predict_churn(data: ChurnRequest):
    # Convert request to DataFrame (sklearn expects column names)
    df = pd.DataFrame([data.dict()], columns=FEATURE_COLUMNS)
    
    proba = model.predict_proba(df)[0][1]  # probability of churn
    prediction = int(proba > 0.5)
    return prediction, float(proba)
