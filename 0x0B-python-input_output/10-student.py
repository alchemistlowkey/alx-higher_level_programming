#!/usr/bin/python3
"""
Student class
"""


class Student:
    """
    A class that defines a Student
    """

    def __init__(self, first_name, last_name, age):
        """
        initialization method for Student class

        Attributes:
            first_name: The first name of the student
            last_name: The last name of the student
            age: The age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Represents of Student into json format

        Return:
            Student class as a json format
        """

        if attrs is None:
            return self.__dict__
        js = {}
        for i in attrs:
            if i in self.__dict__:
                json_dict[i] = self.__dict__[i]
        return js
