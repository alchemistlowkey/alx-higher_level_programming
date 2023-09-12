#!/usr/bin/python3
"""
JSON String
"""
import json


def from_json_string(my_str):
    """
    A function that returns an object (Python data structure)

    Args
        my_str: JSON string

    Returns:
        Python data structure
    """

    return json.loads(my_str)
