#!/usr/bin/python3
""" user class
"""

################################################################################
#CHEPE:
#if you're having issues with your configuration let me know. i can help you.
#make a separate branch and edit that in order to get it to work with your own
#setup. the principle here is don't make your own issues the public's problem
#burn after reading (if you've read this delete it)
################################################################################

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    '''
    creating a table naming it users
    columns for email, password, first and last name.
    All strings and email and password cannot be nullable,
    while first and last name can be nullable
    '''
    ########################################
    #chepe:
    #documentation comments are for describing
    #to the end-user in straight-forward language
    #what the purpose and behaviour of this code is
    #it is not NOT for task management
    #burn after reading
    ########################################
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

        places = relationship(
                "Place",
                back_populates="user",
                casceade="all, delete-orphan")

        reviews = relationship(
                "Review",
                back_populates="user",
                cascade="all, delete_orphan")

        ########################################
        #chepe:
        #remember to delete your own working comments
        #burn after reading
        ########################################

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
