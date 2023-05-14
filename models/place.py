from models.base_model import BaseModel


class NewPlace(BaseModel):
    """NewPlace class for representing a location"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_of_rooms = 0
    number_of_bathrooms = 0
    maximum_guests = 0
    price_per_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialize NewPlace object"""
        super().__init__(self, *args, **kwargs)

    def __str__(self):
        """Returns string representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at"""
        super().save(self)

    def to_dict(self):
        """Returns a dictionary containing all keys and values"""
        return super().to_dict(self)

    def delete(self):
        """Deletes the current instance from the storage"""
        super().delete(self)


if __name__ == "__main__":
    pass
