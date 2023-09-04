#!/usr/bin/python3
"""
A Rectangle Class
"""


class Rectangle:
    """
    A Rectangle class
    Public class attribute of number of instances
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle instance
        Using the public Class attribute to increment the counter

        Attributes:
            width: The width of the rectangle
            height: The height of the rectangle
        """

        self.width = width
        self.height = height

        type(self).number_of_instances += 1

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
            my_string = "\n".join(
                    [str(self.print_symbol) * self.__width] * self.__height)
            return my_string

    def __repr__(self):
        """
        repr method to print rectangle

        Returns:
            The string representation
        """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        The delete method for Rectangle
        Using counter for decrement
        print "Bye Rectangle"
        """

        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method to compare 2 rectangles

        Args:
            rect_1 (class Rectangle): The first Rectangle
            rect_2 (class Rectangle): The second Rectangle

        Returns:
            The biggest or equal rectangle

        Raises:
            TypeError: if either rect 1 or 2 are not instance of rectangle
        """

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
