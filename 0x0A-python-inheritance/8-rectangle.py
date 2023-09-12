#!/usr/bin/python3
"""
Rectangle sub class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle subclass of BaseGeometry.

    Attributes:
        __width: The width of the rectangle.
        __height: The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.

        Raises:
            TypError: If width or height is not an integer
            ValueError: If width or height is less than or equal to 0.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
