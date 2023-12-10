#!/usr/bin/python3
"""
Unit Test Module for the User class
"""

import unittest 
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """Test Cases for the USer Class."""
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_instantiation(self):
        """Tests instantiation of USer Class"""
        user = User()
        self.assertIsInstance(user, User)
    
    def test_user_inheritance(self):
        """Test USer inheritance from BaseModel""" 
        user = User()
        self.assertTrue(issubclass(User, BaseModel))
        
if __name__ == "__main__":
    unittest.main()
