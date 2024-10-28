#!/usr/bin/python3
"""
City class that inherits from BaseModel
"""

################################################################################
#CHEPE:
#run the command i gave you, clear your db beforehand because previously
#built tables might not match the updated models
################################################################################

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

        places = relationship(
                "Place",
                cascade="all, delete-orphan")

    else:
        name = ""
        state_id = ""
