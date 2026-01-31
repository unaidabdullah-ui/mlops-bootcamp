import matplotlib.pyplot as plt
import pandas as pd

from PY_04 import df
# Simple line plot
x = [1,2,3,4,5]
y = [10,20,15,25,30]

plt.figure(figsize=(6,4))
plt.plot(x, y)
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Bar plot
plt.figure(figsize=(6,4))
plt.bar(df["Name"], df["Salary"])
plt.title("Salary by Name")
plt.show()
