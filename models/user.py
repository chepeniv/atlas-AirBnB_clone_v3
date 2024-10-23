#!/usr/bin/python3
""" user class
"""
# Ariel- grabbing column and string data types from sqlalchemy 
# also importing base from file base_model in models folder

from sqlalchemy import Column, String
import models.base_model as basemodel, Base

# Ariel - base inherited, kept syntax from chepe
class User(basemodel.BaseModel, base.BaseModel):
    # Ariel - class attributes
    __tablename_ = users
    
    # Ariel - using column containing a string with 128 char
    # email and password cannot be name, where as first and last name can be null
    
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    
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
