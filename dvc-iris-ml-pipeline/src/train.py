import pandas as pd
import yaml
import pickle
from sklearn.ensemble import RandomForestClassifier

params = yaml.safe_load(open("params.yaml"))["train"]

train = pd.read_csv("data/train.csv")

X = train.drop("species", axis=1)
y = train["species"]

model = RandomForestClassifier(
    n_estimators=params["n_estimators"],
    max_depth=params["max_depth"],
    random_state=params["random_state"]
)

model.fit(X, y)

with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained!")
