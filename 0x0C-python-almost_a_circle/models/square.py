#!/usr/bin/python3
"""
Class Square(Subclass of Rectangle)
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A Grandchild class of class Base
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor of Square class

        Atrributes:
            size: size of the square PIA
            x: Private Instance attribute
            y: Private Instance attribute
            id: privtae instance attribute from the Base class
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Size getter

        Returns:
            The width
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        Size setter

        Args:
            value: size value to be assigned

        Raises:
            TypeError: If value is not an integer
            ValueError: if value <= 0
        """

        self.width = value
        self.height = value

    def __str__(self):
        """
        A special method

        Returns:
            The string representation of the square.
        """

        a = ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                              self.id, self.x, self.y,
                                              self.width))
        return a

    def update(self, *args, **kwargs):
        """
        An update to the public method

        Attributes:
            Args: Arguments to the square class
            kwargs: Key worded arguments to the square class
        """

        if len(args) != 0 and args is not None:
            for position, argument in enumerate(args, 0):
                if position == 0:
                    self.id = argument
                elif position == 1:
                    self.size = argument
                elif position == 2:
                    self.x = argument
                elif position == 3:
                    self.y = argument

        else:
            for keys, values in kwargs.items():
                setattr(self, keys, values)

    def to_dictionary(self):
        """
        A public method that returns the dictionary representation

        Returns:
            The dictionary representation of a Square
        """

        dic_sq = {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
        return dic_sq
