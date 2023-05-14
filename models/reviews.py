from models.base_model import BaseModel

class ReviewModel(BaseModel):
    """A model to represent user reviews"""

    place_id = ""
    user_id = ""
    review_text = ""

    def __init__(self, *args, **kwargs):
        """Instantiates a new ReviewModel object"""
        super().__init__(self, *args, **kwargs)

    def __str__(self):
        """Returns a string representation of the ReviewModel object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the 'updated_at' attribute of the ReviewModel object"""
        super().save(self)

    def to_dict(self):
        """Returns a dictionary containing all keys and values of the ReviewModel object"""
        return super().to_dict(self)

    def delete(self):
        """Deletes the current instance of the ReviewModel object from storage"""
        super().delete(self)


if __name__ == "__main__":
    pass
