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

    with open(filename, encoding="utf-8") as fr:
        fileread = fr.read()
        print(fileread, end="")
