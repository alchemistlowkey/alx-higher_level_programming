#!/usr/bin/python3
"""
A Square subclass of Rectangle(Grandchild)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A Square subclass of Rectangle.

    Attributes:
        __size: The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Suare instance

        Args:
            size: The dimension of the square.

        Raises:
            TypError: If size is not an integer
            ValueError: If size is less than or equal to 0.
        """

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        A function that calculates the area of the square.

        Returns:
            The area of the square.
        """

        solution = self.__size * self.__size
        return solution
