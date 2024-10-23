#!/usr/bin/python3

"""
State class that inherits from BaseModel
"""

from models.base_model import BaseModel


# inherit frob BaseModel and then from Base
class State(BaseModel):
    """
    State class that inherits from BaseModel
    Public class attributes:
        name: string - empty string
    """
    # __tablename__ = "states"
    # name : 128 chars, not null
    # in DBStorage :
    #       cities represents a relationship with class Cities
    #       if State objects is deleted so must all of its Cities
    #       reference from City to State should be named state
    # in FileStorage:
    #       getter attr should return a list of City instances associated with state_id = State.id
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(*args, **kwargs)
        else:
            super().__init__()
            self.name = ""
