from fastapi import FastAPI
from fastapi.responses import Response
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest
import joblib

model = joblib.load("models/model.pkl")
app = FastAPI()

PREDICTIONS = Counter("predictions_total", "Number of predictions served")
LATENCY = Histogram("prediction_latency_seconds", "Time spent on model.predict")

@app.get("/")
def root():
    return {"message": "Welcome to the ML Model API"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(features: list[float]):
    with LATENCY.time():
        prediction = model.predict([features])[0]
    PREDICTIONS.inc()
    return {"prediction": int(prediction)}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
