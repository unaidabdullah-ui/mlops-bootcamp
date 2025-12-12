import pandas as pd
import pickle
import json
from sklearn.metrics import accuracy_score

test = pd.read_csv("data/test.csv")

X = test.drop("species", axis=1)
y = test["species"]

model = pickle.load(open("models/model.pkl", "rb"))

preds = model.predict(X)
acc = accuracy_score(y, preds)

with open("metrics.json", "w") as f:
    json.dump({"accuracy": acc}, f)

print("Accuracy:", acc)
