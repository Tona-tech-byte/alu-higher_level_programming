#!/usr/bin/python3
"""Defines the Base class."""
import json


class Base:
    """Base class for managing IDs and JSON serialization."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON serialization of objects to a file."""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        dictionaries = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set from a dictionary."""
        instance = cls(1, 1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                dictionaries = cls.from_json_string(file.read())
        except IOError:
            return []
        return [cls.create(**dictionary) for dictionary in dictionaries]
