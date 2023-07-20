#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    pow_matrix = matrix.copy()
    for i in range(len(matrix)):
        pow_matrix[i] = list(map(lambda x: x**2, matrix[i]))
    return (pow_matrix)
