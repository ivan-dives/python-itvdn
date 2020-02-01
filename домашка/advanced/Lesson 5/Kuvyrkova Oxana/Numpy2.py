import numpy as np

a = np.array(range(144), int)
matrix = a.reshape(12, 12)
new_m = matrix.transpose()
matrix2 = np.linalg.matrix_power(new_m, 2)
matrix3 = matrix2.dot(2)
one = np.eye(12)
matrix4 = np.subtract(matrix3, one)

print(matrix4)