#!/usr/bin/python3
"""
Unit Test Module for the Amenity class    
"""


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_instantiation(self):
        """Tests instantiation of Amenity Class"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
    
    def test_amenity_inheritance(self):
        """Test Amenity inheritance from BaseModel""" 
        amenity = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))
    
    
if __name__ == "__main__":
    unittest.main()
    