#!/usr/bin/python3

"""
Contains FileStorage class
"""

import json
import os
from importlib import import_module
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    This class handles the storage of hbnb models in JSON format.
    """
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """
        Creates a new FileStorage instance.
        """
        self.model_classes = {
            'BaseModel': import_module('models.base_model').BaseModel,
            'User': import_module('models.user').User,
            'State': import_module('models.state').State,
            'City': import_module('models.city').City,
            'Amenity': import_module('models.amenity').Amenity,
            'Place': import_module('models.place').Place,
            'Review': import_module('models.review').Review
        }

    def all(self, cls=None):
        """
        Provides a dictionary containing the models currently stored.
        """
        if cls is None:
            return self.__objects
        else:
            filtered_dict = {}
            for key, value in self.__objects.items():
                if type(value) is cls:
                    filtered_dict[key] = value
            return filtered_dict

    def delete(self, obj=None):
        """
        Deletes an object from the storage dictionary.
        """
        if obj is not None:
            obj_key = obj.to_dict()['__class__'] + '.' + obj.id
            if obj_key in self.__objects.keys():
                del self.__objects[obj_key]

    def new(self, obj):
        """
        Inserts a new object into the storage dictionary.
        """
        self.__objects.update(
            {obj.to_dict()['__class__'] + '.' + obj.id: obj}
        )

    def save(self):
        """
        Writes the storage dictionary to a file
        """
        with open(self.__file_path, 'w') as file:
            temp = {}
            for key, val in self.__objects.items():
                temp[key] = val.to_dict()
            json.dump(temp, file)

    def reload(self):
        """
        Reads the storage dictionary from a file.
        """
        classes = self.model_classes
        if os.path.isfile(self.__file_path):
            temp = {}
            with open(self.__file_path, 'r') as file:
                temp = json.load(file)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)

    def close(self):
        """
        Terminates the storage engine.
        """
        self.reload()
