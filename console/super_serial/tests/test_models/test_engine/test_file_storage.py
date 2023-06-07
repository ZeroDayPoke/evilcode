#!/usr/bin/python3
"""Unittest for FileStorage class"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base import BaseModel
import copy


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Set up for the tests"""
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down for each test"""
        self.storage = None
        try:
            os.remove("file.json")
        except:
            pass

    def test_all(self):
        """Test the all method"""
        initial_objects = copy.deepcopy(self.storage.all())
        self.assertIsInstance(initial_objects, dict)

        new_object = BaseModel()
        new_object.save()
        updated_objects = self.storage.all()
        self.assertTrue(len(updated_objects) > len(initial_objects))

    def test_new(self):
        """Test the new method"""
        new_object = BaseModel()
        self.storage.new(new_object)
        self.assertIn(new_object, self.storage.all().values())

    def test_save(self):
        """Test the save method"""
        new_object = BaseModel()
        new_object.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test the reload method"""
        new_object = BaseModel()
        new_object.save()
        self.storage.reload()
        objects = self.storage.all()
        self.assertTrue(any(obj.id == new_object.id for obj in objects.values()))
