#!/usr/bin/python3
"""
Class Base Geometry
"""


class BaseGeometry:
    """
    A base geometry class
    """

    def area(self):
        """
        Public Instance method

        Raises:
            Exception: if the area is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public Instance method

        Args:
            name: value name
            value: value to be passed in integer

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is not greater than 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
