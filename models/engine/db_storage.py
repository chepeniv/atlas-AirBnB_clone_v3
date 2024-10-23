#!/usr/bin/python3
"""
this module handles the mysql database storage backend of
our web service
"""


import os
import sqlalchemy
import importlib
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from datetime import datetime
# import sys
# import MySQLdb
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base


# use python-object_relational_mapping/ as reference
class DBStorage:
    # __objects = {}
    __engine = None
    __session = None
    __environment_var_names = [
            'HBNB_MYSQL_USER',
            'HBNB_MYSQL_PWD',
            'HBNB_MYSQL_HOST', # default localhost
            'HBNB_MYSQL_DB'
            ]

    def __init__(self):
        # creat self.__engine linked to hbnb_dev user and hbnb_dev_db
        #       dialect: mysql, driver: mysqldb
        # retrieve environmnent variables
        # when calling create_engine() set pool_pre_ping=True
        # if HBNB_ENV == test, drop all tables (before loading any data ??)
        pass

    def all(self, search_class=None):
        """ returns a dictionary of objects """
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
        """ adds a new object to the dictionary object with
        the key string <class>.<id>
        """
        # add obj to self.__session
        pass

    def save(self):
        """ serializes objects into a json file """
        # commit all changes from self.__session
        pass

    def reload(self):
        """Deserializes objects from a JSON file."""
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
        """ helper method to construct key for object dictionary """
        return type(obj).__name__ + "." + obj.id
