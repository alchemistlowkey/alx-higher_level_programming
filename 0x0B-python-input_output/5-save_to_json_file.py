#!/usr/bin/python3
"""
JSON String
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an object to a text file using a JSON repr

    Args
        my_str: JSON string
        filename: file name

    Returns:
        Nothing
    """

    with open(filename, mode='w') as f:
        json.dump(my_obj, f)
