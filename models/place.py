from models.base_model import BaseModel
"""Place class"""


class Place(BaseModel):
    """Place class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """Class constructor"""
        super().__init__(*args, **kwargs)

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def to_dict(self):
        """to_dict overwrite"""
        place_dict = super().to_dict()
        place_dict["city_id"] = self.city_id
        place_dict["user_id"] = self.user_id
        place_dict["name"] = self.name
        place_dict["description"] = self.description
        place_dict["number_rooms"] = self.number_rooms
        place_dict["number_bathrooms"] = self.number_bathrooms
        place_dict["max_guest"] = self.max_guest
        place_dict["price_by_night"] = self.price_by_night
        place_dict["latitude"] = self.latitude
        place_dict["longitude"] = self.longitude
        place_dict["amenity_ids"] = self.amenity_ids
        return place_dict