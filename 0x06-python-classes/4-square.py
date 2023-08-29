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
        Private instance attribute
        The __init__ method for initializing the square class

        Args:
            size: (:obj: 'init'): A private instance square size

        """
        self.__size = size

    @property
    def size(self):
        """
        Get the size of the square

        Args:

        Returns:
            The square size
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square and check for exceptions

        Args:
            value: checker

        Raises:
            TypeError: Exception for size type.
            ValueError: Exception for size value.

        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Public Instance method
        The Area method that calculates the area of a square

        Args:

        Returns:
            The Area of a square
        """

        calc = self.__size ** 2
        return calc
