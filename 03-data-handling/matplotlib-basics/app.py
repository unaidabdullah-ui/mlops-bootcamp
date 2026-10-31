import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# ---------------------------
# Load Data
# ---------------------------
df = pd.read_csv('data.csv')

print("\n ---- Data Head ---- \n")
print(df.head())

# Remove missing values
df = df.dropna()

# ---------------------------
# Scatter Plot
# ---------------------------
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='Hours', y='Score')
plt.title('Hours vs Score Scatter Plot')
plt.xlabel('Hours')
plt.ylabel('Score')

plt.savefig('scatter_plot.png')
plt.show()

print("\n ---- Scatter Plot Saved as scatter_plot.png ---- \n")

# ---------------------------
# Linear Regression Model
# ---------------------------
X = df[['Hours']]        # 2D DataFrame ✔
y = df['Score']          # 1D Series ✔

model = LinearRegression()
model.fit(X, y)

print("\n--- MODEL TRAINED ---")
print(f"Slope: {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")

# ---------------------------
# Prediction
# ---------------------------
hours = 5
pred = model.predict(np.array([[hours]]))   # Correct shape ✔

print(f"\nPredicted score for {hours} hours = {pred[0]:.2f}")
