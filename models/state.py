#!/usr/bin/python3
"""
State class that inherits from BaseModel and Base
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    Table name is states
    Public class attributes:
        name: Column: string(128) and cannot be null
        cities: relationship with City
    """

    __tablename__ = "states"

    if BaseModel.storage_type == 'db':
        name = Column(
                String(128),
                nullable=False)

        cities = relationship(
                'City',
                cascade='all, delete')
    else:
        name = ""

        @property
        def cities(self):
            '''
            returns dictionary of cities belonging to this state
            '''
            from models import storage
            from models.city import City
            all_cities = storage.all(City)
            state_cities = {}
            for key, city in all_cities.items():
                if city.state_id == self.id:
                    state_cities.update({key: city})
            return state_cities
