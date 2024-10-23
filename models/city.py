#!/usr/bin/python3
"""
City class that inherits from BaseModel
"""

from models.base_model import BaseModel


# inherit from BaseModel and then from Base
class City(BaseModel):
    """
    City class that inherits from BaseModel
    Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    # __tablename__ = "cities"
    # name : 128 chars, not null
    # state_id : 60 chars, not null, foreign key to state.id
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(*args, **kwargs)
        else:
            super().__init__()
            self.state_id = ""
            self.name = ""
