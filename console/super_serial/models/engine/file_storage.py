#!/usr/bin/env python3
""" FileStorage class """

import json
import os
from models.base import BaseModel
from models.cereal import Cereal


class FileStorage:
    """A class for file storage and serialization/deserialization"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Retrieves the dictionary __objects that represents all objects
        Returns:
            dict: A dictionary of all objects
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the __objects dictionary
        Args:
            obj (BaseModel): The object to be added
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to a JSON file
        """
        with open(self.__file_path, 'w') as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        If the JSON file exists, reads the file and creates the corresponding objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                objs = json.load(file)
                for k, v in objs.items():
                    cls = v['__class__']
                    if cls in [BaseModel.__name__, Cereal.__name__]:
                        self.__objects[k] = globals()[cls](**v)
