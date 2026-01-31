import numpy as np

# Creating arrays
a = np.array([1, 2, 3, 4])
b = np.arange(1, 11, 2)
c = np.linspace(0, 1, 5)

print(a)
print(b)
print(c)

# Array operations
print("Mean:", a.mean())
print("Std:", a.std())
print("Sum:", a.sum())
print("Reshape:", np.reshape(a, (2,2)))

# Matrix multiplication
m1 = np.array([[1,2],[3,4]])
m2 = np.array([[5,6],[7,8]])
print("Matrix Product:\n", np.dot(m1, m2))
