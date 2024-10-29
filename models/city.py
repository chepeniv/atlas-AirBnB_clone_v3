#!/usr/bin/python3
"""
City class that inherits from BaseModel and Base
"""

from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey, Column, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    City class that inherits from BaseModel

    Tablename: cities
    Public class attributes:
        Column: state_id - string is 60 char: it will be the State.id
                cannot be null
        Column: name - string is 128 char and cannot be null
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

        # places linked to Place
        # when deleted, automatically deletes linked places
        places = relationship(
                "Place",
                cascade="all, delete-orphan")

    # if not then name and state_id will be an empty string
    else:
        name = ""
        state_id = ""
