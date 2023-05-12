import json
import models
from datetime import datetime
from uuid import uuid4
"""
Base Model
===========
This model has the Base Model class

Example Usage:
-------------
...

Class:
---

BaseModel:
    The parent class from which all the other models inherit

    Attributes:
        id (str): ID of the object
        created_at (str): When the object was created
        updated_at (str): When the object was last updated

    Methods:
        to_json(): Converts a BaseModel instance into a dictionary
        save(): Saves a BaseModel object to a JSON file
"""


# Beginning of code Starts Here


class BaseModel():

    def __init__(self, **kwargs) -> None:
        """
        Creates an instance

        Args:
            id (str): ID of a object
            created_at (datetime.datetime): When the object was created
            updated_at (datetime.datetime): When the object was updated
        """
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    self.created_at = datetime.fromisoformat(val)
                elif key == 'updated_at':
                    self.updated_at = datetime.fromisoformat(val)
                else:
                    setattr(self, key, val)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self) -> str:
        """String Representation of an instance"""
        return (f"[{type(self)}] ({self.id}) {self.__dict__}")

    def __repr__(self) -> str:
        """Returns String Representation of an instance"""
        return (self.__str__())

    def to_dict(self) -> dict:
        """
        Converts an instance into a python dictionary
        Return:
            dict: dictionary format of the instance
        """
        attrs = vars(self).copy()
        attrs['__class__'] = type(self).__name__
        attrs['created_at'] = self.created_at.isoformat()
        attrs['updated_at'] = self.updated_at.isoformat()
        return (attrs)

    def save(self):
        """
        Saves a BaseModel object into a JSON file

        The JSON file name is derived from the name of the model class.


        Return:
            none
        """
        self.updated_at = datetime.now()
        models.storage.save()
