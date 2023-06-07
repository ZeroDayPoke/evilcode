#!/usr/bin/python3
"""Unittest for console"""
import unittest
import sys
from io import StringIO
from console import SuperSerial
from unittest.mock import create_autospec
from models import storage
from models.base import BaseModel
from models.cereal import Cereal


class TestConsole(unittest.TestCase):
    """This class tests console.py file"""

    def setUp(self):
        """Set up method"""
        self.cli = SuperSerial()

    def create_helper(self, class_name="BaseModel"):
        """Helper method to create an instance"""
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.cli.onecmd('create {}'.format(class_name))
        instance_id = sys.stdout.getvalue()
        sys.stdout = old_stdout
        return instance_id.rstrip()

    def test_do_create(self):
        instance_id = self.create_helper()
        self.assertTrue(instance_id in [obj.id for obj in storage.all().values()])

    def test_do_show(self):
        instance_id = self.create_helper()
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.cli.onecmd('show BaseModel {}'.format(instance_id))
        instance_str = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertTrue(instance_id in instance_str)

    def test_do_destroy(self):
        instance_id = self.create_helper()
        self.cli.onecmd('destroy BaseModel {}'.format(instance_id))
        self.assertFalse(instance_id in [obj.id for obj in storage.all().values()])

    def test_do_all(self):
        instance_id = self.create_helper()
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.cli.onecmd('all BaseModel')
        instance_str = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertTrue(instance_id in instance_str)

    def test_do_update(self):
        instance_id = self.create_helper()
        self.cli.onecmd('update BaseModel {} first_name John'.format(instance_id))
        self.assertEqual(storage.all()["BaseModel.{}".format(instance_id)].first_name, 'John')
