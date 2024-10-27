#!/usr/bin/python3

from models import storage_type
from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class BaseModel:

    storage_type = storage_type

    __table_args__ = {'extend_existing': True}

    id = Column(
            String(60),
            primary_key=True, # implies uniqueness
            nullable=False
            )

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
                if key not in ['__class__', 'id', 'created_at', 'updated_at']:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        obj_str = "[{}] ({}) {}"
        return obj_str.format(type(self).__name__, self.id, self.to_dict())

    def delete(self):
        from models import storage
        storage.delete(self)

    def save(self):
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        obj_dict = {}
        for key, value in self.__dict__.items():
            obj_dict.update({key: value})
        obj_dict.pop('_sa_instance_state', None)
        obj_dict.update({
            '__class__': self.__class__.__name__,
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
            })
        return obj_dict
