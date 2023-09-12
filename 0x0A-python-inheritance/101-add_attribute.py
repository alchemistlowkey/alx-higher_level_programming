#!/usr/bin/python3
"""
Add attributes function
"""


def add_attribute(obj, attr, value):
    """
    A function that adds a new attribute to an object is it's possible.

    Args:
        obj: The object to add the attribute to.
        attr: The attribute name.
        value: The attribute value.

    Raises:
        TypeError: If not possible to add a new attribute.
    """

    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
