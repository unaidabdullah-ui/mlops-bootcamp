# utils.py

import joblib
import os
import datetime

def load_model(path):
    if not os.path.exists(path):
        raise FileNotFoundError("Model file not found. Train the model first.")
    return joblib.load(path)


def log(message):
    """
    Simple logging utility
    Writes logs to logs/app.log
    """
    os.makedirs("logs", exist_ok=True)
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("logs/app.log", "a") as f:
        f.write(f"[{time_stamp}] {message}\n")


def log_prediction_request(features, prediction):
    """Logs prediction calls for monitoring."""
    log(f"Prediction request: {features} → {prediction}")
