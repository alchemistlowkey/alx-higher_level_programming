#!/usr/bin/python3
"""
Lookup function
"""


def lookup(obj):
    """
    A function that returns the list of available attributes and methods

    Args:
        obj: parameter

    Returns:
        A list object
    """

    return dir(obj)
