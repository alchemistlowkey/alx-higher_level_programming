#!/usr/bin/python3
"""
Matrix class
"""


def matrix_divided(matrix, div):
    """
    To divide all elements of a matrix

    Args:
        matrix: list of list of int or float
        div: integer or float to divide for

    Raises:
        TypeError: if elements in matrix and div are not integer or float
        ZeroDivisionError: Exception if divided by 0

    Return:
        The result to divide matrix
    """

    if type(div) not in [int, float] or div != div or\
            abs(div) > 1.797693e+308:
        raise TypeError("div must be a number")
        return matrix
    elif div == 0:
        raise ZeroDivisionError("division by zero")
        return matrix

    if type(matrix) is list:
        copy_matrix = [i[:] for i in matrix]
        for x in range(len(matrix)):
            if x <= len(matrix) - 2 and len(matrix[x]) != len(matrix[x + 1]):
                raise TypeError("Each row of the matrix must have the same" +
                                " size")
                return matrix
            for y in range(len(matrix[x])):
                if type(matrix[x][y]) not in [int, float] or\
                        matrix[x][y] != matrix[x][y] or\
                        abs(matrix[x][y]) > 1.797693e+308:
                    raise TypeError("matrix must be a matrix (list of lists)" +
                                    " of integers/floats")
                    return matrix
                else:
                    copy_matrix[x][y] = round(matrix[x][y] / div, 2)
    else:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
        return matrix

    return copy_matrix
