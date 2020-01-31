import numpy as np

a = np.random.randint(9, size=(12, 12))
tr = a.transpose()
b = np.eye(12, 12, dtype=int)

print(a ** 2 * 2 - b)
