#!/usr/bin/python3
"""This is the state class"""

from models.base_model import BaseModel, Base
from os import environ
import models
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref


class State(BaseModel, Base):
    """Class for State with a name attribute"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    
    if 'HBNB_TYPE_STORAGE' in environ and environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship('City', cascade="all, delete-orphan", backref="state")
    else:
        @property
        def cities(self):
            """Returns a list of cities belonging to the state"""
            city_list = []
            state_id = self.id
            for key, obj in models.storage.all().items():
                if "City" in key and obj.state_id == state_id:
                    city_list.append(obj)
            return city_list
