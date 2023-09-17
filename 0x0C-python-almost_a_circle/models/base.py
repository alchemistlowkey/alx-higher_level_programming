#!/usr/bin/python3
"""
Base
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method for the JSON string representation

        Args:
            list_dictionaries: List of dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method for the JSON string to a file

        Args:
            list_objs: List of instances inherited
        """

        filesave = cls.__name__ + ".json"
        with open(filesave, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dicto = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(dicto)
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Static method for the JSON string representation

        Args:
            json_string: A string representing a list of dictionaries
        """

        if len(json_string) == 0 or json_string is None:
            return []
        else:
            return json.loads(json_string)
