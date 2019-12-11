# Транспонирование матриц
from random import randrange

x = int(input('Enter amount of strings: '))
y = int(input('Enter amount of columns: '))

matrix = [y * [0] for i in range(x)]
for i in range(x):
    for j in range(y):
        matrix[i][j] = randrange(10, 100)
for i in matrix:
    print(i)

print('Transposition')

matrix_t = [x * [0] for i in range(y)]
for i in range(y):
    for j in range(x):
        matrix_t[i][j] = matrix[j][i]
for i in range(y):
    print(matrix_t[i])
