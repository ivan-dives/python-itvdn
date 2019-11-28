#!/usr/bin/python3
# -*- coding: utf-8 -*_

import random

weight = 7
high = 5

matrix1 = [[random.randint(1, 100) for j in range(1, weight+1)] for i in range(1, high+1)]
matrix2 = [[random.randint(1, 100) for j in range(1, high+1)] for i in range(1, weight+1)]


def print_matrix (matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:>6}".format(matrix[i][j]), end="")
        print()


print_matrix(matrix1)
print()
print_matrix(matrix2)
print()

def revert (matrix):
    new_matrix = []
    for i in range(weight):
        lst = []
        for j in range(high):
            lst.append(matrix[j][i])
        new_matrix.append(lst)
    return new_matrix


def revert_single_line(matrix):
    return [[matrix[j][i] for j in range(high)]for i in range(weight)]


def matrix_mult(mat1, mat2):
    if len(mat1) != len(mat2[0]):
        return
    new_matrix = []
    for i in range(len(mat1)):
        lst = []
        for j in range(len(mat2[0])):
            sum = 0
            sum += (mat1[i][j]*mat2[j][i])
            lst.append(sum)
        new_matrix.append(lst)
    return new_matrix



def main():
    print_matrix(revert(matrix1))
    print()
    print_matrix(revert_single_line(matrix1))
    matrix_mult(matrix1, matrix2)
    print()
    print_matrix(matrix_mult(matrix1, matrix2))


if __name__ == '__main__':
    main()



