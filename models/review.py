from models.base_model import BaseModel
"""Review class"""


class Review(BaseModel):
    """Review class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """Class constructor"""
        super().__init__(*args, **kwargs)

    place_id = ""
    user_id = ""
    text = ""

    def to_dict(self):
        """to_dict overwrite"""
        review_dict = super().to_dict()
        review_dict["place_id"] = self.place_id
        review_dict["user_id"] = self.user_id
        review_dict["text"] = self.text
        return review_dict
