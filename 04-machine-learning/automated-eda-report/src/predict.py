import pandas as pd
from utils import load_model

def predict(input_dict):
    df = pd.DataFrame([input_dict])
    model = load_model()
    return model.predict(df)[0]

if __name__ == "__main__":
    sample = {"feature1": 5, "feature2": 10}
    print("Prediction:", predict(sample))
