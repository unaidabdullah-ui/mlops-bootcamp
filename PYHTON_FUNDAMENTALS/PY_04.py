import pandas as pd

# Create a DataFrame
data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [21, 25, 28, 22],
    "Salary": [30000, 45000, 50000, 35000]
}

df = pd.DataFrame(data)
print(df)

# Basic operations
print(df.info())
print(df.describe())

# Filtering
print(df[df["Salary"] >= 40000])

# Adding new column
df["Updated Salary"] = df["Salary"] * 1.10
print(df)

# Handling missing values
df.loc[2, "Age"] = None
print(df)
print(df.fillna(df["Age"].mean()))
