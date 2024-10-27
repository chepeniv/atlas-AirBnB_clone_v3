#!/usr/bin/python3
"""
State class that inherits from BaseModel
"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    State class that inherits from BaseModel
    Public class attributes:
        name: string - empty string
    """

    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if models.storage_type == 'db':
            cities = relationship('City', cascade='all, delete')
        else:
            cities = self.__get_cities

    def __get_cities(self):
        cities = self.storage.all('City')
        for city in cities:
            if city.state_id != self.id:
                cities.pop(city.id)
        return cities
