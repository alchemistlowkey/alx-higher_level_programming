#!/usr/bin/python3
"""
Class Rectangle(Subclass of Base)
"""
from models.base import Base


class Rectangle(Base):
    """
    A derived class of class Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor of Rectangle class

        Atrributes:
            width: width of the rectangle PIA
            height: height of the rectangle PIA
            x: Private Instance attribute
            y: Private Instance attribute
            id: privtae instance attribute from the Base class
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Width getter

        Returns:
            The width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter

        Args:
            value: Width value to be assigned

        Raises:
            TypeError: If value is not an integer
            ValueError: if value <= 0
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
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
            value: The height value of the rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height <= 0
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        Retrieves the x property

        Returns:
            x: The x of the rectangle
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x of the rectangle

        Args:
            value: The x value of the rectangle

        Raises:
            TypeError: If x is not an integer
            ValueError: If x < 0
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        Retrieves the y property

        Returns:
            y: The y of the rectangle
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y of the rectangle

        Args:
            value: The y value of the rectangle

        Raises:
            TypeError: If y is not an integer
            ValueError: If y is less than 0
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        A function that returns the area value

        Returns:
            The Area of the rectangle
        """

        area_rect = self.width * self.height
        return area_rect

    def display(self):
        """
        A function that prints # character for area of the rectangle
        """

        for col in range(self.y):
            print()
        for col in range(self.height):
            for row in range(self.x):
                print(" ", end="")
            for row in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
        A special method

        Returns:
            The string representation of the rectangle.
        """

        a = ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                     self.x, self.y,
                                                     self.width,
                                                     self.height))
        return a

    def update(self, *args, **kwargs):
        """
        An update to the public method

        Attributes:
            Args: Arguments to the rectangle class
            kwargs: Key worded arguments to the rectangle class
        """

        if args is not None and len(args) != 0:
            for position, argument in enumerate(args, 0):
                if position == 0:
                    self.id = argument
                elif position == 1:
                    self.width = argument
                elif position == 2:
                    self.height = argument
                elif position == 3:
                    self.x = argument
                elif position == 4:
                    self.y = argument

        else:
            for keys, values in kwargs.items():
                setattr(self, keys, values)
