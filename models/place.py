#!/usr/bin/python3
"""
Place class that inherits from BaseModel and Base
"""

import sys
import os

# Ariel
# adding direct pathway so interpreter can find it.
# worked, no other errors found other than Can't connect error 
# which will be manually graded
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
    """
    Public class attributes:
        city_id: string - empty string: it will be the City.id
        user_id: string - empty string: it will be the User.id
        name: string - empty string
        description: string - empty string
        number_rooms: integer - 0
        number_bathrooms: integer - 0
        max_guest: integer - 0
        price_by_night: integer - 0
        latitude: float - 0.0
        longitude: float - 0.0
        amenity_ids: list of string -
            empty list: it will be the list of Amenity.id later
    """

    __tablename__ = 'places'

    if BaseModel.storage_type == 'db':
        city_id = Column(
                String(60),
                ForeignKey('cities.id'),
                nullable=False)

        user_id = Column(
                String(60),
                ForeignKey('users.id'),
                nullable=False)

        name = Column(
                String(128),
                nullable=False)

        description = Column(
                String(1024),
                nullable=True)

        number_of_rooms = Column(
                Integer,
                default=0,
                nullable=False)

        number_of_bathrooms = Column(
                Integer,
                default=0,
                nullable=False)

        max_guest = Column(
                Integer,
                default=0,
                nullable=False)

        price_by_night = Column(
                Integer,
                default=0,
                nullable=False)

        latitude = Column(
                Float,
                nullable=True)

        longitude = Column(
                Float,
                nullable=True)
        
        # Ariel:
        # comment this too test whether it makes a defference
        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        
        # DBStorage: class attribute reviews must represent a relationship with
        # the class Review. If the Place object is deleted,
        # all linked Review objects must be automatically deleted.
        # Also, the reference from a Review object to 
        # Place should be named place
        
        reviews = relationship("Review", back_populates="place",
                               cascade="all, delete_orphan")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_of_rooms = 0
        number_of_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0

        # Ariel: 
        # will work on where to put this since it needs to be in a function
        # think the loop is throwing it off

    @property
    def reviews(self):
            '''
            '''    
        return storage.get_reviews_by_place_id(self.id)
