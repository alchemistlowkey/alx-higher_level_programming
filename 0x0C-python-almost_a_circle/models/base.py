#!/usr/bin/python3
"""
Base class
"""
import json
import csv


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
            return "[]"
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

    @classmethod
    def create(cls, **dictionary):
        """
        Class method for the instance with all attributes already set

        Args:
            dictionary: The key worded argument for the create class method
        """

        if cls.__name__ == "Rectangle":
            dummy_dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_dummy = cls(1)
        else:
            dummy_dummy = None

        if dummy_dummy is not None:
            dummy_dummy.update(**dictionary)
        return dummy_dummy

    @classmethod
    def load_from_file(cls):
        """
        Class method for the list of instances
        """

        fileload = cls.__name__ + ".json"
        dic = []
        try:
            with open(fileload, encoding="utf-8") as f:
                dic = cls.from_json_string(f.read())
                ret = [cls.create(**dictionary) for dictionary in dic]
                return ret
        except FileNotFoundError:
            return dic

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves to file in CSV

        Args:
            list_objs: List of instances
        """

        filecsv = cls.__name__ + ".csv"
        emp_csv = []
        with open(filecsv, "w", newline="") as f:
            if len(list_objs) == 0 or list_objs is None:
                f.write(emp_csv)
            else:
                new = csv.writer(f)
                if cls.__name__ == "Rectangle":
                    for i in list_objs:
                        list_i = [i.id, i.width, i.height, i.x, i.y]
                        new.writerow(list_i)
                elif cls.__name__ == "Square":
                    for i in list_objs:
                        list_i = [i.id, i.size, i.x, i.y]
                        new.writerow(list_i)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes to load from a CSV file
        """

        filecsv = cls.__name__ + ".csv"
        emp_csv = []
        try:
            with open(filecsv, newline="") as f:
                if cls.__name__ == "Rectangle":
                    new = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    new = ["id", "size", "x", "y"]
                new_instance = csv.DictReader(f, fieldnames=new)
                new_instance = [dict([key, int(value)] for key, value in
                                data.items()) for data in new_instance]
                return [cls.create(**data) for data in new_instance]
        except FileNotFoundError:
            return emp_csv
