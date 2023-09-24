#!/usr/bin/python3
"""
The state class
"""
from sqlalchemy import Column, String
import models
from models.base_model import BaseModel, Base
import shlex
from sqlalchemy.orm import relationship
from os import environ as env


class State(BaseModel, Base):
    """The class for State
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
        """
        Retrieve all cities with the current state
        ID from FileStorage
        """

        var = models.storage.all()
        list = []
        results = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                list.append(var[key])
        for elem in list:
            if (elem.state_id == self.id):
                results.append(elem)
        return (results)
