#!/usr/bin/python3
""" user class
"""

import sys
import os

# Ariel
# adding direct pathway so interpreter can find it.
# worked, no other errors found other than Can't connect error 
# which will be manually graded
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    '''
    Ariel:
    creating a table naming it users
    columns for email, password, first and last name.
    All strings and email and password cannot be nullable,
    while first and last name can be nullable
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
        # Ariel:
        # Add or replace in the class User:
        # class attribute places must represent a
        # relationship with the class Place.
        # If the User object is deleted, all linked Place objects
        # must be automatically deleted.
        # Also, the reference from a Place object to User should be named user
        
        places = relationship("Place", back_populates="user",
                              casceade="all, delete-orphan")
        
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
