from models.base_model import BaseModel
"""User class"""


class User(BaseModel):
    """User class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """CLass Constructor"""
        super().__init__(*args, **kwargs)

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def to_dict(self):
        """to_dict overwrite"""
        user_dict = super().to_dict()
        user_dict["email"] = self.email
        user_dict["password"] = self.password
        user_dict["first_name"] = self.first_name
        user_dict["last_name"] = self.last_name
        return user_dict
