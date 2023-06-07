#!/usr/bin/python3
"""Unittest for Cereal class"""

import unittest
from models.cereal import Cereal
from models.base import BaseModel


class TestCereal(unittest.TestCase):
    """Test the Cereal class"""

    def setUp(self):
        """Set up for the tests"""
        self.cereal_attrs = {
            'name': 'Cereal 19',
            'sugar_content': 99.99,
            'fiber_content': 199.99,
            'is_gluten_free': True,
            'expiration_date': '2012-12-12',
            'shelf_life_days': 365,
            'flavor_complexity': str(complex(2, 3)),
            'other_cereals': ['Sugar Loops', 'Serial Saccharides']
        }
        self.cereal = Cereal(**self.cereal_attrs)

    def test_init(self):
        """Test the initialization"""
        for attr, value in self.cereal_attrs.items():
            with self.subTest(attr=attr, value=value):
                self.assertEqual(getattr(self.cereal, attr), value)

    def test_to_dict(self):
        """Test the to_dict method"""
        cereal_dict = self.cereal.to_dict()
        for attr, value in self.cereal_attrs.items():
            with self.subTest(attr=attr, value=value):
                self.assertEqual(cereal_dict[attr], value)
        self.assertEqual(cereal_dict['__class__'], 'Cereal')

    def test_inheritance(self):
        """Test that Cereal class inherits from BaseModel"""
        self.assertIsInstance(self.cereal, BaseModel)


if __name__ == "__main__":
    unittest.main()
