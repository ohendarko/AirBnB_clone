#!/usr/bin/python3
import json
# from models.base_model import BaseModel
"""
Contains a class FileStorage that 
serializes instances to a JSON file
and deserializes JSON file to instances:
"""
class FileStorage():
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances:
    """
    def __init__(self, file_path="file.json", objects=None):
        self.__file_path = file_path
        self.__objects = objects or {}

    def all(self):
        """
         Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with
        key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to
        the JSON file (path: __file_path)
        """
        to_be_serialized = {}
        for key, obj in self.__objects.items():
            to_be_serialized[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(to_be_serialized, f)

    def reload(self):
        """
        deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            import datetime
            from models.base_model import BaseModel
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                loaded_object = json.load(f)
                for key,obj_dict in loaded_object.items():
                    class_name, obj_id = key.split('.')
                    obj = BaseModel(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass