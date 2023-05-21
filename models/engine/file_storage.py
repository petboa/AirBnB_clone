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
            __file_path(str) -> JSON filename
            __objects(dict) -> keeps all instances
            based in the id of its class
            models(dict) -> Inventory of all models
    """
    __file_path = 'file.json'
    __objects: dict = {}
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
        sets in __objects the obj
        with its <class name>.id as its key
        """

        key = f'{obj.__class__.__name__}.{str(obj.id)}'
        self.__class__.__objects[key] = obj

    def all(self):
        """Return the elements in __objects dictionary
        """
        return (self.__class__.__objects)

    def save(self):
        """
        serializes __objects dict into a JSON file
        (path: __file_path)
        """
        objects_dict = {}
        for key, value in self.__class__.__objects.items():
            objects_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='UTF-8') as f:
            json.dump(objects_dict, f)

    def reload(self):
        """Reloads the stored objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            # TODO: should this overwrite or insert?
            FileStorage.__objects = obj_dict
