from models.base_model import BaseModel
"""City class"""


class City(BaseModel):
    """City class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    state_id = ""
    name = ""