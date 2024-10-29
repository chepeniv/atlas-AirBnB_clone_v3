#!/usr/bin/python3
""" user class
that inherits from basemodel and base
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    '''
    creating a table naming it users
    columns for email, password, first and last name.
    All attributes are strings
    email and password cannot be nullable
    while first and last name can be null
    '''

    __tablename__ = 'users'

    if BaseModel.storage_type == 'db':
        email = Column(
                String(128),
                nullable=False)

        password = Column(
                String(128),
                nullable=False)

        first_name = Column(
                String(128),
                nullable=True)

        last_name = Column(
                String(128),
                nullable=True)

        # places linked to Place and deletes all that references it
        places = relationship(
                "Place",
                cascade="all, delete-orphan")

        # reviews linked to Review and deletes all that references it
        reviews = relationship(
                "Review",
                cascade="all, delete-orphan")

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
