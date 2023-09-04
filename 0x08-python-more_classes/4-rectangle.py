#!/usr/bin/python3
"""
A Rectangle Class
"""


class Rectangle:
    """
    A Rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle instance

        Attributes:
            width: The width of the rectangle
            height: The height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width property

        Returns:
            width: The width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

        Args:
            value (int): The width value of the rectangle

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Retrieves the height property

        Returns:
            height: The height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle

        Args:
            value (int): The height value of the rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Public Instance Method
        Calculates the area of the rectangle

        Returns:
            The area of the rectangle
        """

        areaa = self.__width * self.__height
        return areaa

    def perimeter(self):
        """
        Public instance method
        Calculates the perimeter of the rectangle

        Returns:
            The perimeter of the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0

        peri = 2 * (self.__width + self.__height)
        return peri

    def __str__(self):
        """
        str method to print rectangle

        Returns:
            The string with # rectangle
        """

        my_string = ""
        if self.__width == 0 or self.__height == 0:
            return my_string
        else:
            my_string = "\n".join(["#" * self.__width] * self.__height)
            return my_string

    def __repr__(self):
        """
        repr method to print rectangle

        Returns:
            The string representation
        """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
