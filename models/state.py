#!/usr/bin/python3
"""
State Class from Models Module
"""
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float

storage_type = os.environ.get('HBNB_TYPE_STORAGE')

class State(BaseModel, Base):
    """State class handles all application states"""
    
    if storage_type == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='delete')
    
    else:
        name = ''

class StateFileStorage(State):
    """
    State class with a file storage implementation for 'cities' property
    """
    @property
    def cities(self):
        """
        Getter method, returns a list of City objects from storage
        linked to the current State
        """
        city_list = []
        for city in models.storage.all("City").values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
