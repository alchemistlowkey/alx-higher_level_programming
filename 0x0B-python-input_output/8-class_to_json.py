#!/usr/bin/python3
"""
JSON representation of an object(string)
"""


def class_to_json(obj):
    """
    A function that returns the dictionary description with data structure

    Args:
        obj: The object input to create a class

    Return:
        A JSON representation
    """

    js = {}
    for att in obj.__dict__:
        if not att.startswith("__"):
            value = getattr(obj, att)
            if isinstance(value, (list, dict, str, int, bool)):
                js[att] = value
    return js
