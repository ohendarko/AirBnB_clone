from models.base_model import BaseModel
"""State class"""


class State(BaseModel):
    """State class that inherits from BaseModel"""
    def __init__(self, name="", *args, **kwargs):
        """Class constructor"""
        super().__init__(*args, **kwargs)
        self.name = name

    def to_dict(self):
        """to_dict overwrite"""
        state_dict = super().to_dict()
        state_dict["name"] = self.name
        return state_dict
