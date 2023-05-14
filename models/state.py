# Importing the BaseModel class from models.base_model
from models.base_model import BaseModel

# Defining a State class that inherits from BaseModel
class State(BaseModel):
    """A class to represent the state of an object"""
    name = ""

    # Instantiating the State object
    def __init__(self, *args, **kwargs):
        """Initializes a State object"""
        super().__init__(self, *args, **kwargs)

    # String representation of the State object
    def __str__(self):
        """Returns a string representation of the State object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    # Saves the State object
    def save(self):
        """Updates the public instance attribute updated_at"""
        super().save(self)

    # Returns a dictionary containing all keys/values of the State object
    def to_dict(self):
        """Returns a dictionary containing all keys/values of the State object"""
        return super().to_dict(self)

    # Deletes the State object
    def delete(self):
        """Deletes the current instance from the storage"""
        super().delete(self)

# Main program
if __name__ == "__main__":
    # Do nothing
    pass
