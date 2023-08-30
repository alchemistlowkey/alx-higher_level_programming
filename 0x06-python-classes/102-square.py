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
        self.size = size

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

    def __eq__(self, other):
        """
        Compare two squares in terms of area.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the squares are equal in area.

        """

        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare if two squares are not equal in terms of area.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the squares are not equal in area.

        """

        return self.area() != other.area()

    def __gt__(self, other):
        """
        Compare if one square is greater in terms of area.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the current square is greater in area.

        """

        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare if one square is greater than or equal to the other

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the current square is greater than or equal

        """

        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Compare if one square is less than the other in terms of area.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the current square is less in area

        """

        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare if one square is less than or equal to the other.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the current square is less than or equal in area.

        """

        return self.area() <= other.area()
