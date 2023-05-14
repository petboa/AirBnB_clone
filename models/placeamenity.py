import base_model

class PlaceAmenityModel(base_model.BaseModel):
    """Class representing the relationship between a place and an amenity"""
    place_id = ""
    amenity_id = ""

    def __init__(self, *args, **kwargs):
        """Instantiates a new PlaceAmenityModel"""
        super().__init__(self, *args, **kwargs)

    def __str__(self):
        """Returns a string representation of the PlaceAmenityModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the public instance attribute 'updated_at'"""
        super().save(self)

    def to_dict(self):
        """Returns a dictionary containing all keys and values"""
        return super().to_dict(self)

    def delete(self):
        """Deletes the current instance from the storage"""
        super().delete(self)

if __name__ == "__main__":
    pass
