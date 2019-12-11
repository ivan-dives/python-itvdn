# Перемножение матриц
from random import randrange

x1 = int(input('Enter amount of strings for 1st matrix: '))
y1 = int(input('Enter amount of columns for 1st matrix (strings for 2nd matrix): '))
y2 = int(input('Enter amount of columns for 2nd matrix: '))
x2 = y1

matrix1 = [y1 * [0] for i in range(x1)]
matrix2 = [y2 * [0] for j in range(x2)]
result = [y2 * [0] for l in range(x1)]

# First and second matrices
for i in range(x1):
    for j in range(y1):
        matrix1[i][j] = randrange(0, 10)
for i in range(x2):
    for j in range(y2):
        matrix2[i][j] = randrange(0, 10)

#  Multiplication
for z in range(x1):
    for x in range(y2):
        for c in range(y1):
            result[z][x] += matrix1[z][c] * matrix2[c][x]

print('First matrix:')
for i in matrix1:
    print(i)
print('\nSecond matrix:')
for i in matrix2:
    print(i)
print('\nMultiplication')
for i in result:
    print(i)







# matrix_t = [x * [0] for i in range(y)]
# for i in range(y):
#     for j in range(x):
#         matrix_t[i][j] = matrix[j][i]
# for i in range(y):
#     print(matrix_t[i])
