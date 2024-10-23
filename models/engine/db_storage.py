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
from sqlalchemy.orm import sessionmaker


class DBStorage:
    # __objects = {}
    __engine = None
    __session = None

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
        Session = sessionmaker(self.__engine)
        if env == "test":
            Base.metadata.drop_all(self.__engine)
        self.__session = Session()


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
        # add obj to self.__session
        pass

    def save(self):
        """
        """
        # commit all changes from self.__session
        pass

    def reload(self):
        """
        """
        # create all tables in the database (sqlalchemy)
        # ALL classes that inherit from Base MUST be imported before calling Base.metadata.create_all(engine)
        # create self.__session from self.__engine using sessionmaker
        #       expire_on_commit=False
        #       set scope_session to ensure the session is thread-safe
        pass

    def delete(self, obj=None):
        """
        remove the given object from __objects if it exist within
        if nothing is given do nothing
        """
        # if not None, delete obj from self.__session
        if obj == None:
            return
        else:
            pass

    def construct_key(self, obj):
        """
        helper method to construct key for object dictionary
        """
        return type(obj).__name__ + "." + obj.id
