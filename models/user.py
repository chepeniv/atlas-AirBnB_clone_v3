#!/usr/bin/python3
""" user class
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    '''
    add documentation
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
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
    # ARIEL
    # create relationship with places to Place using relationship
    # if user is deleted all linked place will auto delete using cascade
    # refer Place to User called user using back_populates
    # places = relationship("Place", back_populates="user",
    #                     cascade="all, delete-orphan")
