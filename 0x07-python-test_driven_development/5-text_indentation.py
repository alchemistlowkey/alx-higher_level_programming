#!/usr/bin/python3
"""
Test Printing with special characters condition
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after '.', '?', and ':'

    Args:
        text: text to print

    Raises:
        TypeError: text must be a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    word = text.replace('.', '.\n\n').replace(':', ':\n\n')\
        .replace('?', '?\n\n')

    for char in range(len(text)):
        word = word.replace('\n ', '\n')

    print(word, end='')
