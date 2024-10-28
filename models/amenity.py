#!/usr/bin/python3
"""
Amenity class that inherits from BaseModel
"""

from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey, Column, String


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
    else:
        name = ""
