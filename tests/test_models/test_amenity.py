#!/usr/bin/python3
"""Amenities test suite"""
#import os
#import models
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class Test_Amenity(unittest.TestCase):
    """Amemities test"""

    def setUp(self):
         print("Testing Amenity model")

    def test_name_amenities(self):
        """Name input test"""
        pass

    def test_Amenity_is_basemodelSubclass(self):
         amt = Amenity()
         self.assertIsInstance(amt, BaseModel)

    def test_Amenity_isInstance(self):
         amt = Amenity()
         self.assertIsInstance(amt, Amenity)

    def test_Amenity_twoIds(self):
         amt = Amenity()
         amy = Amenity()
         self.assertNotEqual(amt.id, amy.id)

    def test_Amenity_threeIds(self):
         amn = Amenity()
         amt = Amenity()
         amy = Amenity()
         self.assertNotEqual(amy.id, amn.id)

    def test_Amenity_timeCreated(self):
         amn = Amenity()
         amt = Amenity()
         self.assertNotEqual(amn.created_at, amt.created_at)

    def test_Amenity_timeUpdated(self):
         amn = Amenity()
         amt = Amenity()
         self.assertNotEqual(amn.updated_at, amt.updated_at)

    def test_Amenity_nameid_default_value(self):
         amt = Amenity()
         self.assertEqual(amt.name, "")


if __name__ == '__main__':
        unittest.main()
