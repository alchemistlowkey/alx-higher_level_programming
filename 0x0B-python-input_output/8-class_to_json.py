#!/usr/bin/python3
"""
JSON representation of an object(string)
"""
import json


def class_to_json(obj):
    """
    A function that returns the dictionary description with data structure

    Args:
        obj: The object input to create a class

    Return:
        A JSON representation
    """

    return {key: value for (key, value) in obj.__dict__.items()
            if key in list(obj.__dict__.keys())}
