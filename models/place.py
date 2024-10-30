#!/usr/bin/python3
"""
Place class that inherits from BaseModel and Base
"""

from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import MetaData
from models.base_model import BaseModel, Base
import models

# import metadata to create an instance for SQLAlchemy table
metadata_obj = Base.metadata

# add instance of SQL ALchemy table called place_amenity
# Ariel@ SideNote: need to see if this is the right orientation for this table
place_amenity = Table("place_amenity", Base.metadata,
                              Column("place_id", String(60),
                                     ForeignKey("places.id"), primary_key=True,
                                     nullable=False),
                              Column("amenity_id", String(60),
                                     ForeignKey("amenities.id"),
                                     primary_key=True, nullable=False))
class Place(BaseModel, Base):
    """
    Table name: places

    Public class attributes:
        Column: city_id - string of 60 char
                it will be the City.id cannot be null
        Column: user_id - string of 60 char
                it will be the User.id cannot be null
        Column: name - string of 128 char, cannot be null
        Column: description - string 1024 char, can be null
        Column: number_rooms - integer, defaults to 0
                cannot be null
        Column: number_bathrooms - integer, defaults to 0
                cannot be null
        Column: max_guest - integer, defaults to 0
                cannot be null
        Column: price_by_night - integer, defaults to 0
                cannot be null
        Column: latitude - float, can be null
        Column: longitude- float, can be null

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

        number_rooms = Column(
                Integer,
                default=0,
                nullable=False)

        number_bathrooms = Column(
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

        # creates link from reviews to Review, when deleted, automatically
        # deletes all linked reviews
        reviews = relationship(
                "Review",
                cascade="all, delete-orphan")

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

    if models.storage_type == 'db':
            amenities = relationship('Amenity', secondary=place_amenity,
                                     viewonly=False)
    else:
            amenity_ids = []

        # getter for aminities in FileStorage 
    @property
    def amenities(self):
        if models.storage_type == 'db':
                return self.amenities
                return [amenity for amenity in
                    models.storage.all('Amenity').values() if amenity.id
                    in self.amenity_ids]
        
        # setter for amenities in FileStorage
        @amenities.setter
        def amenities(self, obj):
                if models.storage_type != 'db' and isinstance(obj, models.Amenity):
                        if obj.id not in self.amenity_ids:
                        # Ariel@chepe:
                        # this indentation will throw flake8 all over the place if it's moved.
                        # Tried different variations but nothing is happy
                        self.amenity_ids.append(obj.id)
                
            
        # method that acts as an attribute
        # retrieves all instances of Review class
        @property
        def reviews(self):
            reviews = self.storage.all('Review')
            for review in reviews:
                if review.place_id != self.id:
                    reviews.pop(review.id)
            return reviews
