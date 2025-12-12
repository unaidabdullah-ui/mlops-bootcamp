import pandas as pd
import yaml
from sklearn.model_selection import train_test_split

params = yaml.safe_load(open("params.yaml"))["split"]

df = pd.read_csv("data/raw/iris.csv")

train, test = train_test_split(df, test_size=params["test_size"], random_state=42)

train.to_csv("data/train.csv", index=False)
test.to_csv("data/test.csv", index=False)

print("Data prepared!")
