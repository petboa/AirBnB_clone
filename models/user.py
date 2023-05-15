from models.base_model import BaseModel

class User(BaseModel):
    """Class representing a user"""

    email_address = ""
    user_password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new User instance"""
        super().__init__(self, *args, **kwargs)

    def __str__(self):
        """Returns a string representation of a User object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at"""
        super().save(self)

    def to_dict(self):
        """Returns a dictionary representation of a User object"""
        return super().to_dict(self)

    def delete(self):
        """Deletes the current instance from the storage"""
        super().delete(self)


if __name__ == "__main__":
    pass
