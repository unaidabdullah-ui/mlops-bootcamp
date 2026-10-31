import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import os
import pickle
import yaml

params = yaml.safe_load(open("params.yaml"))["train"]

df = pd.read_csv("data/processed/processed.csv")

X = df[['Hours']]
y = df['Score']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=params["test_size"],
    random_state=params["random_state"]
)

model = LinearRegression()
model.fit(X_train, y_train)

os.makedirs(os.path.dirname(params["model_output"]), exist_ok=True)
with open(params["model_output"], "wb") as f:
    pickle.dump(model, f)
