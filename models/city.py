"""
City Model

===========
This model has the City Model class

Example Usage:
-------------
...

Class:
---

City:
    Inherits from BaseModel class

"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City Class
    attributes:
        state_id (str) -> State.id
        name (str) -> Name of the City
    """
    name = ""
    state_id = ""
