#!/usr/bin/env python3
"""This module contains the BaseModel class."""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    A base class for other models in the ABNB Clone - Console Project.
    
    Attributes:
        id (str): Unique id for each BaseModel.
        created_at (datetime): The date and time when an instance is created.
        updated_at (datetime): The date and time when an instance is updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid4())
                self.created_at = self.updated_at = datetime.now()
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: String representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
        created_at and updated_at are converted to string objects in ISO format.

        Returns:
            dict: Dictionary containing the keys/values of the instance.
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        if "flavor_complexity" in dict_copy:
            dict_copy["flavor_complexity"] = str(self.flavor_complexity)
        return dict_copy
