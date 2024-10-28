#!/usr/bin/python3
"""
Review class that inherits from BaseModel
"""


from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey, Column, String


class Review(BaseModel, Base):
    """
    Review class that inherits from BaseModel
    Public class attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    __tablename__ = 'reviews'

    if BaseModel.storage_type == 'db':
        text = Column(
                String(1024),
                nullable=False)
    else:
        text = ""
