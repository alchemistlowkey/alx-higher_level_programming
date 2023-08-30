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

    def __init__(self, size=0, position=(0, 0)):
        """
        Private instance attribute
        The __init__ method for initializing the square class

        Args:
            size: (:obj: 'init'): A private instance square size
            position: (:obj: 'tuple', optional): A PIP

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the size of the square

        Args:

        Returns:
            The square size
        """

        return self.__size

    @property
    def position(self):
        """
        Get the position

        Args:

        Returns:
            Tuple position
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        Setter position attribute and check for exceptions

        Args:
            value: checker

        Raises:
            TypeError: Exception for position value
        """

        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def my_print(self):
        """
        Public Instance method
        prints in stdout the square with the character #

        Args:

        Returns:
            Nothing
        """

        if self.__size == 0:
            print()
        else:
            for x in range(self.position[1]):
                print()
            for x in range(self.size):
                for i in range(self.position[0]):
                    print(end=" ")
                for j in range(self.size):
                    print("#", end="")
                print()

    def __str__(self):
        """
        A string repesentation of the square.

        Returns:
            str: The string representation.

        """

        sq_str = ""

        if self.__size == 0:
            return sq_str

        for i in range(self.position[1]):
            sq_str += "\n"
        for i in range(self.size):
            for a in range(self.position[0]):
                sq_str += " "
            for b in range(self.size):
                sq_str += "#"
            sq_str += "\n"
        return sq_str.rstrip()
