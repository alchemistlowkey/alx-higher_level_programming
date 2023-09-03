#!/usr/bin/python3
"""
Addition function of two numbers
Returns the sum of the numbers in int
"""


def add_integer(a, b=98):
    """
    Adds 2 numbers integers or floats

    Args:
        a: 1st argument
        b: 2nd argument with default value of 98

    Returns:
        Integer: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer of float

    """

    if type(a) is not int:
        if type(a) is float and a == a and abs(a) <= 1.797693e+308:
            a = int(a)
        else:
            raise TypeError("a must be an integer")

    if type(b) is not int:
        if type(b) is float and b == b and abs(b) <= 1.797693e+308:
            b = int(b)
        else:
            raise TypeError("b must be an integer")

    return a + b
