#!/usr/bin/python3
"""
This module defines a class for managing file storage
in the context of an hbnb clone.
"""
import json


class FileStorage:
    """
    This class oversees the storage of hbnb models in
    JSON format.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Provides a dictionary containing the models
        currently stored.
        """
        if cls is not None:
            sortedObjs = {}
            for key, value in FileStorage.__objects.items():
                if type(value) == cls:
                    sortedObjs[key] = value
            return sortedObjs
        return FileStorage.__objects

    def new(self, obj):
        """
        Inserts a new object into the storage dictionary
        """
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """
        Saves the storage dictionary to a file.
        """
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """
        Loads the storage dictionary from a file.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review
        from models.city import City


        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Removes the object from __objects if it is not None.
        """
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del FileStorage.__objects[key]

    def close(self):
        """ 
        Calls the reload() method to deserialize the JSON
        file into objects
        """
        self.reload()
