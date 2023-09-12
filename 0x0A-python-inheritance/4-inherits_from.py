#!/usr/bin/python3
"""
Inheritance
"""


def inherits_from(obj, a_class):
    """
    A function to check if an object is an instance of a class

    Args:
        obj: object
        a_class: class

    Returns:
        True or False
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
