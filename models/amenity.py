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
    __tablename__ = "cities"

    name = Column(
            String(128),
            nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
