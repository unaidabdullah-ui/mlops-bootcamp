import pandas as pd
import joblib

def load_data(path):
    return pd.read_csv(path)

def save_model(model,path="models/model.pkl"):
    joblib.dump(model, path)    
def load_model(path="models/model.pkl"):
    return joblib.load(path)