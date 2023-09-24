#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
from os import environ
from sqlalchemy import Table, Text

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    if 'HBNB_TYPE_STORAGE' in environ and environ['HBNB_TYPE_STORAGE'] == 'db':
        reviews = relationship('Review', backref="places")
        amenities = relationship('Amenity',
                                 secondary="place_amenity",
                                 back_populates='place_amenities',
                                 viewonly=False)
    else:
        lis = []

        @property
        def review(self):
            stat = self.id
            for k, v in models.storage.all().items():
                if "Review" in k and v.state_id == self.id:
                    lis.append(v)
            return lis

        @property
        def amenities(self):
            stat = self.id
            for k, v in models.storage.all().items():
                if "Amenity" in k and v.amenity_id == self.id:
                    lis.append(v)
            return lis

        @amenities.setter
        def amenities(self, value):
            if value.__class__.__name__ == "Amenity":
                self.amenity_id.append(str(value.id))
