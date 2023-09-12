#!/usr/bin/python3
"""
MyInt subclass of int
"""


class MyInt(int):
    """
    MyInt derivedclass int.
    """

    def __eq__(self, value):
        """
        Override the equality operator (==) to inverted form

        Args:
            value: The value to compare with.

        Returns:
            True if not equal, False if equal.
        """

        return super().__ne__(value)

    def __ne__(self, value):
        """
        Override the equality operator (!=) to inverted form.

        Args:
            value: The value to compare with.

        Returns:
            True if not equal, False if equal.
        """
        return super().__eq__(value)
