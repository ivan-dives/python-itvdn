matrix = [
[1,2,3,4,5],
[6,7,8,9,10],
[11,12,13,14,15]
]

a = len(matrix)
b = len(matrix[0])
matrix2 =[[]*3 for i in range (5)]  # create matrix 3x5

for i in list(range(a)):
    for j in list(range(b)):
        matrix2[j].append(matrix[i][j])  # pull numbers in matrix to matrix2

print(matrix2)