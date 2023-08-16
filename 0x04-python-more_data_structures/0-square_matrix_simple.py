#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()
    for values in range(len(matrix)):
        new[values] = list(map((lambda x: x ** 2), matrix[values]))
    return new
