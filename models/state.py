#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ as env
import models
import shlex


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        __tablename__: table name
        name: input name
        cities: relation to cities table
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")


    @property
    def cities(self):
        """get all cities with the current state id
        from filestorage or custom storage if not DBStorage
        """
        from models import storage  # Import the storage module

        if storage.__class__.__name__ != 'DBStorage':
            # If storage is not DBStorage, use custom retrieval logic
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

        # If storage is DBStorage, rely on the relationship
        # defined in the SQLAlchemy model
        return self.cities
