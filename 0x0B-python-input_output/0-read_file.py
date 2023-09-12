#!/usr/bin/python3
"""
Read file
"""


def read_file(filename=""):
    """
    A function that reads a text file and prints to stdout

    Args:
        filename: the file name that accepts the file read

    Returns:
        Nothing
    """

    with open("my_file_0.txt", encoding="utf-8") as f:
        filename = f.read()
        print(filename, end="")
