#!/usr/bin/python3

from models import storage
from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class BaseModel:

    id = Column(
            String(60),
            primary_key=True, # implies uniqueness
            nullable=False
            )

    # default value on DateTime types might simply be enforced by __init__
    created_at = Column(
            DateTime,
            nullable=False
            )

    updated_at = Column(
            DateTime,
            nullable=False
            )

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = kwargs.get('id')
            created_at = kwargs.get('created_at')
            updated_at = kwargs.get('updated_at')

            if type(created_at) is str:
                self.created_at = datetime.fromisoformat(created_at)
            else:
                self.created_at = datetime.now()

            if type(updated_at) is str:
                self.updated_at = datetime.fromisoformat(updated_at)
            else:
                self.updated_at = datetime.now()

            for key, value in kwargs.items():
                if key not in ['id', 'created_at', 'updated_at']:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        obj_str = "[{}] ({}) {}"
        return obj_str.format(type(self).__name__, self.id, self.__dict__)

    def delete(self):
        storage.delete(self)

    def save(self):
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        # remove _sa_instance_state from the dictionary returned if it exist
        obj_dict = self.__dict__.copy()
        obj_dict.update({
            '__class__': self.__class__.__name__,
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
            })
        return obj_dict
