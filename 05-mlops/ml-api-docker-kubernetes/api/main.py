from fastapi import FastAPI
import joblib
import numpy as np
import time

model = joblib.load("models/model.pkl")
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the ML Model API"}

@app.post("/predict")
def predict(features:list):
    start = time.time()

    prediction = model.predict([features])[0]
    
    latency = time.time() - start
    with open("metrics.txt", "w") as f:
        f.write(f"prediction_latency {latency}")
    
    return {"prediction": int(prediction), "latency": latency}

          