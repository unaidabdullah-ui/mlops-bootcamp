# predict.py

import joblib
import numpy as np
import pandas as pd
from src.utils import load_model

model = load_model("models/model.pkl")

def predict_single(features):
    """
    features → list of numbers
    Example: [3.5, 1.2, 0.8]
    """
    prediction = model.predict([features])[0]
    return int(prediction)

def predict_csv(csv_path):
    df = pd.read_csv(csv_path)
    preds = model.predict(df)
    return preds.tolist()

if __name__ == "__main__":
    # Example usage
    print("Predict single:", predict_single([3.5, 1.2, 0.8]))
