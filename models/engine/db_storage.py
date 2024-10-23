#!/usr/bin/python3
"""
this module handles the mysql database storage backend of
our web service
"""


import os
import sqlalchemy
import importlib
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    # __objects = {}
    __engine = None
    __session = None
    __session_generator = None

    def __init__(self):
        env = os.environ.get('HBNB_ENV')
        env_user = os.environ.get('HBNB_MYSOL_USER', 'hbnb_dev')
        env_user_pwd = os.environ.get('HBNB_MYSOL_PWD', 'hbnb_dev_pwd')
        env_host = os.environ.get('HBNB_MYSOL_HOST', 'localhost')
        env_db = os.environ.get('HBNB_MYSOL_DB', 'hbnb_dev_db')

        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(
                env_user, env_user_pwd, env_host, env_db)
        self.__engine = create_engine(db_url, pool_pre_ping=True)
        # all classes that inherit from Base must be imported calling create_all()
        Base.metadata.create_all(self.__engine)
        self.__session_generator = sessionmaker(self.__engine, expire_on_commit=False)
        if env == "test":
            Base.metadata.drop_all(self.__engine)
        self.__session = self.__session_generator()


    def all(self, search_class=None):
        """
        returns a dictionary of objects based on the class given
        """
        # query self.__session to extract all objects of the class search_class
        # return a dictionary (like that of FileStorage)
        #       with elements of the form <class>.<id>: <object>
        if search_class == None:
            return self.__objects
        else:
            class_name = search_class.__name__
            objects_of_class = {}
            for (key, value) in self.__objects.items():
                if key.find(class_name) == 0:
                    objects_of_class.update({key: value})
            return objects_of_class

    def new(self, obj):
        """
        adds a new object to the dictionary object with
        the key string <class>.<id>
        """
        # this might just be enough, since obj would 
        # presumably already be mapped to the database table
        self.__session.add(obj)

    def save(self):
        """
        save all changes onto to the database
        """
        self.__session.commit()

    def reload(self):
        """
        """
        # create all tables in the database (sqlalchemy)
        # use Session.refresh() ?
        self.__session.close()
        Base.metadata.create_all(self.__engine)
        new_session = scoped_session(self.__session_generator)
        self.__session = new_session()

    def delete(self, obj=None):
        """
        remove the given object from __objects if it exist within
        if nothing is given do nothing
        """
        if obj == None:
            return
        else:
            ObjClass = type(obj)
            (self
             .__session
             .query(ObjClass)
             .filter(ObjClass.id == obj.id)
             .delete(synchronize_session=False))

    def construct_key(self, obj):
        """
        helper method to construct key for object dictionary
        """
        return type(obj).__name__ + "." + obj.id
