#!/usr/bin/python3
"""
Created a class called MagicClass
"""

import math


class MagicClass:
    """
    Magicclass for a circle
    """
    def __init__(self, radius=0):
        """
        Initialization of the MagicClass

        Args:
            Radius(float, optional): The Radius of the magic circle

        Raises:
            TypeError: Exception for type

        """

        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the magic circle

        Returns:
            float: float value
        """

        area_of_circle = (self.__radius ** 2) * math.pi
        return area_of_circle

    def circumference(self):
        """
        Calculates the perimeter of the magic circle

        Returns:
            float: float value
        """

        perimeter = 2 * math.pi * self.__radius
        return perimeter
