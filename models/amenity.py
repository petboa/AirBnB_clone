from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    This class represents an amenity.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Instantiates an Amenity object.
        """
        super().__init__(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the Amenity object.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at.
        """
        super().save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys and values.
        """
        return super().to_dict()

    def delete(self):
        """
        Deletes the current instance from the storage.
        """
        super().delete()

if __name__ == "__main__":
    pass
