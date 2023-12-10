#!/usr/bin/python3
"""
Unit Test Module for the City class    
"""


import unittest
from models.base_model import BaseModel
from models.city import City

class TestCity(unittest.TestCase):
    """Test cases for the City class"""
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_instantiation(self):
        """Tests instantiation of City Class"""
        city = City()
        self.assertIsInstance(city, City)
    
    def test_city_inheritance(self):
        """Test City inheritance from BaseModel""" 
        city = City()
        self.assertTrue(issubclass(City, BaseModel))
    
    
if __name__ == "__main__":
    unittest.main()
    