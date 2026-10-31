import os
import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

if __name__ == "__main__":
    df = load_data("data/raw/students.csv")
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/processed.csv", index=False)
