#!/usr/bin/python3
"""
Unit Test Module for the Review class    
"""


import unittest
from models.base_model import BaseModel
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for the Review class"""
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_instantiation(self):
        """Tests instantiation of Review Class"""
        review = Review()
        self.assertIsInstance(review, Review)
    
    def test_review_inheritance(self):
        """Test Review inheritance from BaseModel""" 
        review = Review()
        self.assertTrue(issubclass(Review, BaseModel))
    
    
if __name__ == "__main__":
    unittest.main()
    