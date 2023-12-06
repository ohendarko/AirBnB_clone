#!/usr/bin/python3
from datetime import datetime
import uuid
"""
This contains a class BaseModel that
defines all common attributes/methods for other classes
"""
class BaseModel():
    """
    Defines all common attributes/methods
    for other classes
    """
    def __init__(self, *args, kwargs):
        if not kwargs or "id" not in kwargs:
            self.id = str(uuid.uuid4())
        else:
            self.id = kwargs["id"]
        self.created_at = self.updated_at = datetime.now()
    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {str(self.__dict__)}"


    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()


    def to_dict(self):
        """
        returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary