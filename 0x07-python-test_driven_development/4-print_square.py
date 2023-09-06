#!/usr/bin/python3
"""
Square printing with #
"""


def print_square(size):
    """
    prints a square of size=size with character #

    Args:
        size: size of the square to print

    Raises:
        TypeError: Size is not an integer
        ValueError: Size is less than 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for dimension in range(size):
        print('#'*size)
