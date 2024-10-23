#!/usr/bin/python3
"""
this module handles the mysql database storage backend of
our web service
"""

import importlib
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from datetime import datetime


# import sqlalchemy
# import MySQLdb ?
# use python-object_relational_mapping/ as reference
class DBStorage:
    # create private class attributes:
    # __engine = None
    # __session = None
    __file_path = "file.json"
    __objects = {}

    # create public class methods:
    # __init__(self)
    #       create engine self.engine 
    #           linked to hbnb_dev user and hbnb_dev_db
    #       retrieve environmnent variables
    #           HBNB_MYSQL_USER
    #           HBNB_MYSQL_PWD
    #           HBNB_MYSQL_HOST default localhost ?
    #           HBNB_MYSQL_DB
    #       when calling create_engine() set pool_pre_ping=True
    #       if HBNB_ENV == test, drop all tables (afterwards ?)

    def all(self, search_class=None):
        """ returns a dictionary of objects """
        # query self.__session to extract all objects of the class search_class
        # if search_class=None return all objects
        # elements must be in the form <class>.<id>: <object>
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
        key = self.construct_key(obj)
        self.__objects.update({key: obj})

    def save(self):
        """ serializes objects into a json file """
        # commit all changes to self.__session
        decomposed = {}
        for key, obj in self.__objects.items():
            obj_dict = obj.to_dict()
            decomposed.update({key: obj_dict})

        json_string = json.dumps(decomposed)
        try:
            json_file = open(self.__file_path, "w")
            json_file.write(json_string)
            json_file.close()
        except FileNotFoundError:
            pass

    def reload(self):
        """Deserializes objects from a JSON file."""
        # create all tables in the database (sqlalchemy)
        # ALL classes that inherit from Base MUST be imported before calling Base.metadata.create_all(engine)
        # create self.__session from self.__engine using sessionmaker
        #       expire_on_commit=False
        #       set scope_session to ensure the session is thread-safe
        try:
            json_file = open(self.__file_path, 'r')
            json_data = json_file.read()
            json_file.close()
            extracted_data = json.loads(json_data)

            for key, value in extracted_data.items():
                model_class = value['__class__']
                model_class = globals().get(model_class)
                if model_class is not None:
                    obj = model_class(**value)
                    self.__objects.update({key: obj})

        except FileNotFoundError:
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
            key = self.construct_key(obj)
            if self.__objects.get(key) is not None:
                self.__objects.pop(key)

    def construct_key(self, obj):
        """ helper method to construct key for object dictionary """
        return type(obj).__name__ + "." + obj.id
