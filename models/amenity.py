from models.base_model import BaseModel
"""Amenity class"""


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel"""
    def __init__(self, name="", *args, **kwargs):
        """Class constructor"""
        super().__init__(*args, **kwargs)
        self.name = name

    def to_dict(self):
        """to_dict overwrite"""
        amenity_dict = super().to_dict()
        amenity_dict["name"] = self.name
        return amenity_dict