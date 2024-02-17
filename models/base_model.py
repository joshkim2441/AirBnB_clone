#!/usr/bin/python3
""""
The base class that defines the BaseModel
to serve the entire project
"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ The base class for all other classes """

    def __init__(self, *args, **kwargs):
        """ Initializes public instance attributes """
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            return
        """ Deserialization """
        if 'id' not in kwargs:
            kwargs['id'] = str(uuid4())
        self.id = kwargs['id']

        for key, val in kwargs.items():
            if key == "__class__":
                continue
        if "created_at" in kwargs:
            self.created_at = datetime.strptime(
                kwargs['created_at'],
                '%Y-%m-%dT%H:%M:%S.%f')
        if "updated_at" in kwargs:
            self.updated_at = datetime.strptime(
                kwargs['updated_at'],
                '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """
        Return string representation of the class
        name, id and the dictionary
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def __repr__(self):
        """ Returns the string representation """
        return (self.__str__())

    def save(self):
        """
        Updates the public instance attribute
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary contanining all
        key-values of the __dict_- instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()

        return dict_copy
