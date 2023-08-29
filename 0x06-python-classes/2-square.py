#!/usr/bin/python3
"""
Created a class square
"""


class Square:
    """
    A square is a shape with equal dimensions

    Attributes:
        size (int): The size of the square
    """

    def __init__(self, size=0):
        """
        The __init__ method for initializing the square class

        Args:
            size: (:obj: 'init'): A private instance square size

        Raises:
            TypeError: Exception for size type.
            ValueError: Exception for size value.

        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
