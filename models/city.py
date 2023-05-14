from models.base_model import BaseModel

class City(BaseModel):
    """Represents a city"""

    def __init__(self, *args, **kwargs):
        """Initializes a new City instance"""
        super().__init__(self, *args, **kwargs)
        self.state_id = ""
        self.name = ""

    def __str__(self):
        """Returns a string representation of the City instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at"""
        super().save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values"""
        return super().to_dict()

    def delete(self):
        """Deletes the current instance from the storage"""
        super().delete()


if __name__ == "__main__":
    pass
