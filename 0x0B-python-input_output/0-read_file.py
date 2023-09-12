#!/usr/bin/python3
"""
Read file
"""


def read_file(filename=""):
    with open("my_file_0.txt", encoding="utf-8") as f:
        filename = f.read()
        print(filename, end="")
