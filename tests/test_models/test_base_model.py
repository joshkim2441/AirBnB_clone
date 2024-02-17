#!/usr/bin/env python3
""" A vase model unittest """

import unittest
import json
import uuid
from models.base_model import BaseModel
from datetime import datetime
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestBaseModel(unittest.TestCase):
    """ Base model unittests """

    def setUp(self):
        """ The proceeding tests setup """
        self.model = BaseModel()
        self.model.name = "My First Model"
        self.model.my_number = 89

    def test_id_type(self):
        """ Id type test """
        self.assertEqual(type(self.model.id), str)

    def test_created_at_type(self):
            """ Created_at type test """
            self.assertEqual(type(self.model.created_at), datetime)

    def test_updated_at_type(self):
        """ Updated_at type test """
        self.assertEqual(type(self.model.updated_at), datetime)

    def test_name_type(self):
        """ Name_type test """
        self.assertEqual(type(self.model.name), str)

    def test_my_number_type(self):
        """ My_number type test """
        self.assertEqual(type(self.model.my_number), int)
