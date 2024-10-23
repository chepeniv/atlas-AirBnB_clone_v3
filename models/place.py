#!/usr/bin/python3
"""
Place class that inherits from BaseModel
"""
# importing mysqlalchemy datatypes
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

# import Base to inherift from
from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
    """
    Place class that inherits from BaseModel
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
    # adding class attributes along with column, string, foreignkey
    # and whether or not it can be null
    ##########
    # New code -Ariel
    ##########
    
    __tablename__ = places
    
    city_id = Column(String(60), ForeignKey(cities.id), nullable=False)
    user_id = Column(String(60), ForeignKey(users.id), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_of_rooms = Column(Integer, default=0, nullable=False)
    number_of_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullabe=True)
    longitude = Column(Float, nullable=True)
    
    ##########
    #Old code
    ##########
    
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(*args, **kwargs)
        else:
            super().__init__()
            self.city_id = ""
            self.user_id = ""
            self.name = ""
            self.description = ""
            self.number_rooms = 0
            self.number_bathrooms = 0
            self.max_guest = 0
            self.price_by_night = 0
            self.latitude = 0.0
            self.longitude = 0.0
            self.amenity_ids = []
