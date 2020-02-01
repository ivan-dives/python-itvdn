import numpy as np

matrix = np.arange(625).reshape(25, 25)
one = np.eye(25)
np.dot(one, matrix)
print(np.dot(one, matrix))