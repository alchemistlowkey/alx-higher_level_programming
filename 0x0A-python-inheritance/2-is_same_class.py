#!/usr/bin/python3
"""
Inheritance
"""


def is_same_class(obj, a_class):
    """
    A function to check if an object is an instance

    Args:
        obj: object
        a_class: class

    Returns:
        True or False
    """

    return type(obj) is a_class
