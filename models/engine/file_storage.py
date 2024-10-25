#!/usr/bin/python3
"""
this module handles the file storage backend of
our web service
"""

import json
from datetime import datetime


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, search_class=None):
        """ returns a dictionary of objects """
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
        key = self.construct_key(obj)
        self.__objects.update({key: obj})

    def save(self):
        """ serializes objects into a json file """
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
        try:
            json_file = open(self.__file_path, 'r')
            json_data = json_file.read()
            json_file.close()
            extracted_data = json.loads(json_data)

            for key, value in extracted_data.items():
                model_class = value['__class__']
                model_class = self.get_model(model_class)
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
        if obj == None:
            return
        else:
            key = self.construct_key(obj)
            if self.__objects.get(key) is not None:
                self.__objects.pop(key)

    def construct_key(self, obj):
        """ helper method to construct key for object dictionary """
        return type(obj).__name__ + "." + obj.id

    def get_model(self, model_class):
        if globals().get(model_class) is None:
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.place import Place
            from models.amenity import Amenity
            from models.review import Review
        return globals().get(model_class)

