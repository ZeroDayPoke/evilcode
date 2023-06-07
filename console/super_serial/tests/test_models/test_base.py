#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
from models.base import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def setUp(self):
        """Set up for the tests"""
        self.base_model = BaseModel()

    def tearDown(self):
        """Tear down for each test"""
        self.base_model = None

    def test_init(self):
        """Test the initialization"""
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_str(self):
        """Test the __str__ method"""
        expected = "[{}] ({}) {}".format(self.base_model.__class__.__name__, self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected)

    def test_save(self):
        """Test the save method"""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], self.base_model.__class__.__name__)
        self.assertEqual(base_model_dict['id'], self.base_model.id)
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIsInstance(base_model_dict['updated_at'], str)
