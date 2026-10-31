import pandas as pd
import pickle
import json
from sklearn.metrics import mean_absolute_error

with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

df = pd.read_csv("data/processed/processed.csv")
X = df[['Hours']]
y = df['Score']

preds = model.predict(X)
mae = mean_absolute_error(y, preds)

with open("metrics.json", "w") as f:
    json.dump({"mae": mae}, f)
