#!/usr/bin/python3
from datetime import datetime
import uuid
from models import storage
# change
"""
This contains a class BaseModel that
defines all common attributes/methods for other classes
"""


class BaseModel():
    """
    Defines all common attributes/methods
    for other classes
    """
    fmt = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """constructor format allows for flexibility"""
        fmt = "%Y-%m-%dT%H:%M:%S.%f"
        # if key=value pairs not provided as arguments or
        # a key named "id" is not part of **kwargs:
        #     create a unique id
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.strptime(value, self.fmt))
                    else:
                        setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

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
        storage.save()

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
