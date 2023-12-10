from models.base_model import BaseModel
"""User class"""


class User(BaseModel):
    """User class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    email = ""
    password = ""
    first_name = ""
    last_name = ""