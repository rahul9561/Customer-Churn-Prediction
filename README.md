<!-- @format -->

# Customer Churn Prediction

A full-stack project to predict customer churn using a
**RandomForestClassifier** with **FastAPI** backend.

---

## **Project Structure**

churn_project/
│
├── data/ # Raw dataset (CSV)
│ └── churnData.csv
│
├── models/ # Saved ML model
│ └── churn_model.pkl
│
├── app/
│ ├── init.py
│ ├── main.py # FastAPI app
│ ├── schemas.py # Request/response schema
│ └── utils.py # Model loading + prediction
│
├── train_model.py # Model training + MLflow logging
├── requirements.txt # Python dependencies
├── Dockerfile # Docker configuration
├── .gitignore # Git ignore rules
└── README.md # Project documentation

---

## **Features**

- Predict if a customer will churn.
- Shows probability of churn.
- Uses **RandomForestClassifier**.
- ML metrics logged with **MLflow**.
- Backend built with **FastAPI**.
- Frontend built with **React + Vite**.
- Easy environment variable configuration for API URL.

---

## **Setup Instructions**

### 1️⃣ Backend Setup

1. Clone the repository:

```bash
git clone https://github.com/rahul9561/Customer-Churn-Prediction.git
cd churn_project
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

Train the model:

```bash
python train_model.py
```

Run the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open Swagger UI: http://127.0.0.1:8000/docs
