#!/usr/bin/python3
"""
File append
"""


def append_write(filename="", text=""):
    """
    A function that appends a string to a text file

    Args:
        filename: Name of the file
        text: text to be written
    """

    with open(filename, "a", encoding="utf-8") as fa:
        nb = fa.write(text)
        return nb
