#!/usr/bin/python3
"""
State class that inherits from BaseModel
"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String


class State(BaseModel, Base):
    """
    State class that inherits from BaseModel
    Public class attributes:
        name: string - empty string
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    # likely very unnecessary
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # unclear whether this should be called regardless of storage engine
    # def __del__(self):

    if models.storage_type == 'db':
        cities = self.storage.new(City)
        # cities must represent a relationship with class Cities
        # if State objects is deleted so must all of its Cities
        pass
    else:
        # cities should return a list of City objects whose state_id match this
        #       State.id
        # getter attr should return a list of City instances such that
        #       state_id = State.id
        pass
