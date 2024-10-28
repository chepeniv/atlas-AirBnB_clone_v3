#!/usr/bin/python3
"""
City class that inherits from BaseModel
"""

import sys
import os

# Ariel
# adding direct pathway so interpreter can find it.
# worked, no other errors found other than Can't connect error 
# which will be manually graded
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey, Column, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    Ariel:
    if storage type = db add columns for each attribute
    name and state_id will be strings
    state_id has foreign key tied to states.id
    both cannot be null

    City class that inherits from BaseModel
    Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    __tablename__ = "cities"

    if BaseModel.storage_type == 'db':
        name = Column(
                String(128),
                nullable=False)

        state_id = Column(
                String(60),
                ForeignKey("states.id"),
                nullable=False)
        # Ariel
        # Add or replace in the class City:
        # class attribute places must represent a relationship with the class Place. If the City object is deleted, all linked Place objects must be automatically deleted. 
        # Also, the reference from a Place object to his City should be named cities

        places = relationship("Place", back_populates="cities", cascade="all, delete-orphan")

    else:
        name = ""
        state_id = ""
