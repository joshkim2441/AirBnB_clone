#!/usr/bin/python3
"""
file storage module to serialize and
deserialize JSON types
"""

import os
import json
import models
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class FileStorage:
    """file storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Dictionary representation of all objects"""
        return self.__objects

    def new(self, object):
        """Set the object with the key in __objects"""
        key = "{}.{}".format(object.__class__.__name__, object.id)
        FileStorage.__objects[key] = object

    def save(self):
        """Serialize objects to JSON file"""
        fpath = FileStorage.__file_path

        newObj = {k: FileStorage.__objects[k].to_dict(
        ) for k in FileStorage.__objects.keys()}

        with open(fpath, 'w') as f:
            json.dump(newObj, f)

    def reload(self):
        """Deserializes JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                dict = json.loads(f.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
