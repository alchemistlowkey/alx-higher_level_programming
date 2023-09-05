#!/usr/bin/python3
"""
Name Print Class
"""


def say_my_name(first_name, last_name=""):
    """
    print a full name using the first and last name

    Args:
        first_name: First name string
        last_name: Second name string

    Raises:
        TypeError: Exception if arguments are not string
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
