#!/usr/bin/python3
"""
Base
"""


class Base:
    """
    A Base class of all other classes (Parent class)

    Attributes:
        __nb_objects: Private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor

        Attributes:
            id: Public instance attribute
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
