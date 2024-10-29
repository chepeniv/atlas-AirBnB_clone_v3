#!/usr/bin/python3
"""
Amenity class that inherits from BaseModel, Base
"""

from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey, Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Amenity class that inherits from BaseModel
    Public class attributes:
        name: string - empty string
    """
    __tablename__ = "amenities"

    if BaseModel.storage_type == 'db':
        name = Column(
                String(128),
                nullable=False)
        
        #  create Many to Many relationship between Place and Amenities
        place_amenities = relationship("Place", secondary="Amenity")

    else:
        name = ""
