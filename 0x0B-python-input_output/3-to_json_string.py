#!/usr/bin/python3
"""
JSON representation of an object(string)
"""
import json


def to_json_string(my_obj):
    """
    A function that returns the JSON representation of an object (string)

    Args:
        my_obj: The object to convert to JSON.

    Returns:
        The JSON representation of the object as a string.
    """

    return json.dumps(my_obj)
