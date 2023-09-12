#!/usr/bin/python3
"""
File write
"""


def write_file(filename="", text=""):
    """
    A function that writes a string to a text file

    Args:
        filename: Name of the file
        text: text to be written
    """

    with open(filename, "w", encoding="utf-8") as f:
        nb = f.write(text)
        return nb
