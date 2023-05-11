"""
Amenity Model

===========
This model has the Amenity Model class

Example Usage:
-------------
...

Class:
---

Amenity:
    Inherits from BaseModel class

"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity Class
    attributes:
        name (str) -> Name of the amenity
    """
    name = ""
