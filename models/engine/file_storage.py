#!usr/bin/env python3

"""
File Storage
 Responsible for:
    - serializing objects in a JSON file
    - deserializing objects from a JSON file
"""
import json
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place_amenity import PlaceAmenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    File Storage Engine
        Class Attrs:
            __file_name(str) -> JSON filename
            __instances(dict) -> keeps all instances
            based in the id of its class
            models(dict) -> Inventory of all models
    """
    __file_name = 'storage.json'
    __instances: dict = {}
    models: dict = {
        'BaseModel': BaseModel,
        'Amenity': Amenity,
        'City': City,
        'PlaceAmenity': PlaceAmenity,
        'Place': Place,
        'Review': Review,
        'State': State,
        'User': User
    }

    def new(self, obj):
        """
        sets in __instances the obj
        with its <class name>.id as its key
        """

        key = f'{obj.__class__.__name__}.{str(obj.id)}'
        self.__class__.__instances[key] = obj

    def all(self):
        """Return the elements in __instances dictionary
        """
        return (self.__class__.__instances)

    def save(self):
        """
        serializes __instances dict into a JSON file
        (path: __file_name)
        """
        objects_dict = {}
        for key, value in self.__class__.__instances.items():
            objects_dict[key] = value.to_dict()

        with open(FileStorage.__file_name, 'w', encoding='UTF-8') as storage:
            json.dump(objects_dict, storage, indent=4)

    def reload(self):
        """
        deserializes the JSON file into __instances dict
        (only if the JSON file (ie __file_name) exists)
        does nothing otherwise
        """
        if os.path.exists(FileStorage.__file_name):
            with open(FileStorage.__file_name, 'r', encoding='UTF-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    base = FileStorage.models[value['__class__']](**value)
                    FileStorage.__instances[key] = base
