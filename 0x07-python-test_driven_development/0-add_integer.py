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

    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
