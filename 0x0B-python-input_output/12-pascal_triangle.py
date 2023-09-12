#!/usr/bin/python3
"""
Pascals Triangle
"""


def pascal_triangle(n):
    """
    A function that creates a pascal triangle

    Attributes:
        n: The n exponent for triangle

    Return:
        A matrix with values for the triangle
    """

    pascal = []
    triangle = []

    for i in range(int(n)):
        n = pascal[:]
        n.append(1)
        p = len(pascal)
        for i in range(1, p):
            n[i] = pascal[i - 1] + pascal[i]
        pascal = n[:]
        triangle.append(pascal)
    return triangle
