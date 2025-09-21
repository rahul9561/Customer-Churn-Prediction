from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.schemas import ChurnRequest, ChurnResponse
from app.utils import predict_churn
from app.logger import logger

app = FastAPI(title="Customer Churn Prediction API")

# cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/v1/predict", response_model=ChurnResponse)
def predict(request: ChurnRequest):
    try:
        logger.info(f"Received request: {request.dict()}")
        prediction, proba = predict_churn(request)
        logger.info(f"Prediction result: churn={prediction}, probability={proba:.4f}")
        return ChurnResponse(churn=prediction, probability=proba)
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        return {"error": "Prediction failed. Check logs for details."}
