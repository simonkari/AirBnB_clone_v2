#!/usr/bin/python3
"""
Contains FileStorage class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Amenity": Amenity,
    "State": State,
    "Place": Place,
    "Review": Review,
}

class FileStorage:
    """
    Serializes objects to JSON strings and deserializes
    JSON strings back to objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns the list of objects of one type of class.
        """
        if cls is None:
            return self.__objects
        else:
            new_dict = {}
            for key in self.__objects:
                if cls.__name__ in key:
                    new_dict[key] = self.__objects[key]
            return new_dict

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class>.id.
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path:__file_path).
        """
        object_to_json = {}
        for key in self.__objects:
            object_to_json[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(object_to_json, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects only if the
        file (__file_path) exists.
        """
        try:
            with open(self.__file_path, "r") as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except Exception:
            pass

    def delete(self, obj=None):
        """
        Delete obj from __objects if its inside.
        """
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def close(self):
        """Call reload() method for deserializing the
        JSON file to objects.
        """
        self.reload()
