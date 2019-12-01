from pprint import pprint
matrix = [[5, 0, 7, 4, 6],
          [1, 3, 8, 9, 6],
          [8, 5, 4, 0, 2]]
matrix_t = list(zip(*matrix))

pprint(matrix)
pprint(matrix_t)