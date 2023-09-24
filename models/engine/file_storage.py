#!/usr/bin/python3
"""T
his is the file storage class for AirBnB
"""

import json
from models.base_model import BaseModel, User, State, City, Amenity, Place, Review

class FileStorage:
    """
    This class serializes and deserializes instances
    to/from a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of objects or a filtered
        dictionary by class name.
        """
        if cls:
            return {key: obj for key, obj in self.__objects.items() if type(obj).__name__ == cls.__name__}
        return self.__objects

    def new(self, obj):
        """
        Sets the __objects dictionary with the given object.
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects and saves it to the JSON file.
        """
        my_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to objects and stores
        them in __objects.
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in json.load(f).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes an object from __objects and saves the changes.
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects.pop(key, None)
            self.save()

    def close(self):
        """
        Deserializes the JSON file to objects and stores
        them in __objects.
        """
        self.reload()
