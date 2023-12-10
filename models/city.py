from models.base_model import BaseModel
"""City class"""


class City(BaseModel):
    """City class that inherits from BaseModel"""
    def __init__(self, name="", state_id="", *args, **kwargs):
        """Class constructor"""
        super().__init__(*args, **kwargs)
        self.name = name
        self.state_id = state_id

    def to_dict(self):
        """to_dict overwrite"""
        city_dict = super().to_dict()
        city_dict["name"] = self.name
        city_dict["State.id"] = self.state_id
        return city_dict
