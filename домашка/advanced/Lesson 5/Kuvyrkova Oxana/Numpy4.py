import numpy as np

matrix = np.arange(0, 300).reshape(3, 100)

matrix2 = matrix.copy().reshape(6, 50)
print(matrix2)