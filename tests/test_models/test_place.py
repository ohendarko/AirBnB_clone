#!/usr/bin/python3
"""
Unit Test Module for the Place class    
"""


import unittest
from models.base_model import BaseModel
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_instantiation(self):
        """Tests instantiation of Place Class"""
        place = Place()
        self.assertIsInstance(place, Place)
    
    def test_place_inheritance(self):
        """Test Place inheritance from BaseModel""" 
        place = Place()
        self.assertTrue(issubclass(Place, BaseModel))
    
    
if __name__ == "__main__":
    unittest.main()
    