#!/usr/bin/python3
"""
"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import unittest
import os
import json


class TestDBStorage(unittest.TestCase):
    '''
    '''

    @classmethod
    def test_createclass(cls):
        """
        """
        cls.user = User()
        cls.user.first_name = "Sergio"
        cls.user.last_name = "Zamudio"
        cls.user.email = "whaaaaaat@true.com"
        cls.storage = FileStorage()

    @classmethod
    def test_dele(cls):
        """
        """
        del cls.user

    def test_dele(self):
        """
        """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_n(self):
        """
        """
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = 12345
        user.name = "Karen"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_all(self):
        """
        """
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_rdb(self):
        """
        """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
