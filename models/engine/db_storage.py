#!/usr/bin/python3
"""
This module defines a database storage class for AirBnB clone.
"""

from os import environ, getenv
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City

class DBStorage():
    """
    This class manages database storage for AirBnB clone.
    """

    __engine = None
    __session = None
    supported_classes = [State, City, User, Place, Review, Amenity]

    def __init__(self):
        """
        Initializes a new DBStorage instance.
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if 'HBNB_ENV' in environ and environ['HBNB_ENV'] == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of objects in the database.

        Args:
            cls (str): The class name of objects to retrieve.

        Returns:
            dict: A dictionary of objects.
        """
        objects = {}
        if cls is None:
            for class_name in self.supported_classes:
                rows = self.__session.query(class_name).all()
                for row in rows:
                    key = "{}.{}".format(class_name.__name__, row.id)
                    objects[key] = row
        else:
            rows = self.__session.query(eval(cls)).all()
            for row in rows:
                key = "{}.{}".format(cls, row.id)
                objects[key] = row
        return objects

    def new(self, obj):
        """
        Adds a new object to the current database session.

        Args:
            obj (BaseModel): The object to add to the session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes to the database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the current database session.

        Args:
            obj (BaseModel): The object to delete from the session.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reloads objects from the database.
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)()

    def close(self):
        """
        Closes the current database session.
        """
        self.__session.close()
