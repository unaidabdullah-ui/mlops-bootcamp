import pandas as pd
from utils import load_model

def predict(input_dict):
    df = pd.DataFrame([input_dict])
    model = load_model()
    return model.predict(df)[0]

if __name__ == "__main__":
    sample = {"CustomerID": 21, "Age": 30, "Income": 50000, "MonthlySpend": 1500, "Tenure": 12, "SupportTickets": 3}
    print("Prediction:", predict(sample))
