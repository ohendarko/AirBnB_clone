#!/usr/bin/python3
"""Unittest module for the BaseModel Class"""


from models.base_model import BaseModel
from datetime import datetime
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        print("setUp success")
        pass

    def tearDown(self):
        print("tearDown success")
        pass

    def test_instantiation(self):
        """Tests instantiation of BaseModel class"""
        # Test basic instantiation
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)

    def test_str(self):
        """Tests the __str__ method of the BaseModel class"""
        pass

    def test_save(self):
        """Tests the save method of the BaseModel class"""
        pass
    
    def test_to_dict(self):
        """Tests the to_dict method of the BaseModel class"""

        
if __name__ == '__main__':
    unittest.main()
