import numpy as np

a = np.random.randint(9, size=(25, 25))
print(a)
b = np.eye(25, 25, dtype=int)
print("\n", a*b)
