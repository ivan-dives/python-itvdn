import numpy as np

a = np.random.randint(9, size=300)
print(a)
b = a.reshape(3, 100)
print("\n", b)
c = b.reshape(6, 50)
print("\n", c)
