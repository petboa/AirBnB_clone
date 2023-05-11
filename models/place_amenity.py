#!/usr/bin/python3

"""PlaceAmenity model, inheritting from the BaseModel"""

from models.base_model import BaseModel


class PlaceAmenity(BaseModel):
    """
    PlaceAmenity class
    Attributes:
        place_id str -> location of the amenity
        amenity_id str -> list of strings of ameninty ID's
    """
    place_id = ""
    amenity_id = ""
