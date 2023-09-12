#!/usr/bin/python3
"""
Inheritance
"""


class MyList(list):
    """
    Mylist Class (Derived Class)
    """

    def print_sorted(self):
        """
        Public Instance Method that prints sorted list(ascending order)
        """
        new_list = self[:]
        print(sorted(new_list))
