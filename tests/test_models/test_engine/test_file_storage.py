#!/usr/bin/python3
"""A BaseModel class test module"""
import os
import json
import models
import unittest
from models.city import City
from models.user import User
from datetime import datetime
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_File_Storage(unittest.TestCase):
    """A test class for file storage"""

    def setUp(self):
        """Validaes correct set up"""
        self.storage = FileStorage()

    def test_storage_creation(self):
        """Validates correct creation process"""
        self.assertEqual(self.storage.save(), None)

    def test_storage_instatiationWithArgs(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_instatiationWithNoArgs(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_storage_filePath_isPrivateStr(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_storage_obj_isPrivateDict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storageInitializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class Test_FileStorageMethods(unittest.TestCase):
    """FileStorage class unittest testing methods"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def testAll(self):
        self.assertEqual(dict, type(models.storage.all()))

    def testAll_withArg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def testNew(self):
        bmd = BaseModel()
        usr = User()
        stt = State()
        plc = Place()
        cty = City()
        amy = Amenity()
        rvw = Review()
        models.storage.new(bmd)
        models.storage.new(usr)
        models.storage.new(stt)
        models.storage.new(plc)
        models.storage.new(cty)
        models.storage.new(amy)
        models.storage.new(rvw)
        self.assertIn("BaseModel." + bmd.id, models.storage.all().keys())
        self.assertIn(bmd, models.storage.all().values())
        self.assertIn("User." + usr.id, models.storage.all().keys())
        self.assertIn(usr, models.storage.all().values())
        self.assertIn("State." + stt.id, models.storage.all().keys())
        self.assertIn(stt, models.storage.all().values())
        self.assertIn("Place." + plc.id, models.storage.all().keys())
        self.assertIn(plc, models.storage.all().values())
        self.assertIn("City." + cty.id, models.storage.all().keys())
        self.assertIn(cty, models.storage.all().values())
        self.assertIn("Amenity." + amy.id, models.storage.all().keys())
        self.assertIn(amy, models.storage.all().values())
        self.assertIn("Review." + rvw.id, models.storage.all().keys())
        self.assertIn(rvw, models.storage.all().values())

    def testNew_withArgs(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def testSave(self):
        bmd = BaseModel()
        usr = User()
        stt = State()
        plc = Place()
        cty = City()
        amy = Amenity()
        rvw = Review()
        models.storage.new(bmd)
        models.storage.new(usr)
        models.storage.new(stt)
        models.storage.new(plc)
        models.storage.new(cty)
        models.storage.new(amy)
        models.storage.new(rvw)
        saveText = ""
        with open("file.json", "r") as f:
            saveText = f.read()
            self.assertIn("BaseModel." + bmd.id, saveText)
            self.assertIn("User." + usr.id, saveText)
            self.assertIn("State." + stt.id, saveText)
            self.assertIn("Place." + plc.id, saveText)
            self.assertIn("City." + cty.id, saveText)
            self.assertIn("Amenity." + amy.id, saveText)
            self.assertIn("Review." + rvw.id, saveText)


if __name__ == '__main__':
    unittest.main()
