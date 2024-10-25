#!/usr/bin/python3
""" user class
"""
# Ariel- grabbing column and string data types from sqlalchemy 
# also importing base from file base_model in models folder

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import models.base_model as basemodel
import models.base_model as Base


# Ariel - base inherited, kept syntax from chepe
class User(basemodel, Base):
    # redefining base
    Base = declarative_base()

    # Ariel - class attributes needed for declarative orm
    __tablename__ = 'users'

    # Ariel - using column containing a string with 128 char
    # email and password cannot be name, where as first and last name can be null

    # id = Column(Integer, primary_key=True)
    # created_at = Column(Integer, primary_key=True)
    # updated_at = Column(Integer, primary_key=True)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)


    # ARIEL
    # create relationship with places to Place using relationship
    # if user is deleted all linked place will auto delete using cascade
    # refer Place to User called user using back_populates
    places = relationship("Place", back_populates="user",
                          cascade="all, delete-orphan")

    ####################
    # Older code below
    ####################

    # public class
    # update FileStorage to manange de/serialization of this class
    # update console.py commands to use this class
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(*args, **kwargs)
        else:
            super().__init__()
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""