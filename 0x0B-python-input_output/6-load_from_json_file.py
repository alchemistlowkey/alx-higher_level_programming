#!/usr/bin/python3
"""
JSON representation of an object(string)
"""
import json


def load_from_json_file(filename):
    """
    A function that creates an Object from a “JSON file”

    Args:
        filename: The name of the file

    Returns:
        Object created
    """

    with open(filename, mode='r') as f:
        return json.load(f)
