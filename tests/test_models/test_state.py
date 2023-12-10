#!/usr/bin/python3
"""
Unit Test Module for the State class    
"""


import unittest
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    """Test cases for the State class"""
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_instantiation(self):
        """Tests instantiation of State Class"""
        state = State()
        self.assertIsInstance(state, State)
    
    def test_state_inheritance(self):
        """Test State inheritance from BaseModel""" 
        state = State()
        self.assertTrue(issubclass(State, BaseModel))
    
    
if __name__ == "__main__":
    unittest.main()
    