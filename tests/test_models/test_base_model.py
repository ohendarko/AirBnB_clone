#!/usr/bin/python3
"""
Unit test module for the BaseModel Class.
"""


import unittest
from models.base_model import BaseModel
from datetime import datetime
import time
from models import storage
import os



class TestBaseModel(unittest.TestCase):
    """Test Cases for the BaseModel class"""
    
    def setUp(self):
        """Sets up test methods."""
        pass
    
    def tearDown(self):
        """Tears down test methods."""
        pass
    
    # Reminder: Need to add a method to clear the storage after tests,
    # have it called in the tearDown method.
    
    def test_instantiation(self):
        """Tests instantiation for BAseModel"""
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)
        
    def test_instantiation_kwargs(self):
        """Tests instantiation with kwargs"""
        base_model = BaseModel()
        base_model.name = "Kwadwo"
        base_model.my_number = 100
        base_model_json = base_model.to_dict()
        new_base_model = BaseModel(**base_model_json)
        self.assertEqual(new_base_model.to_dict(), base_model.to_dict())
         
    def test_save(self):
        base_model = BaseModel()
        initial_update_time = base_model.updated_at
        time.sleep(1)
        base_model.save()
        date_now = datetime.now()
        time_diff = date_now - initial_update_time 
        self.assertTrue(time_diff.total_seconds() < 2)
        
    def test_str(self):
        base_model = BaseModel()
        base_model_str = str(base_model)
        self.assertIn('[BaseModel]', base_model_str)
        self.assertIn(base_model.id, base_model_str)
        self.assertIn('created_at', base_model_str)
        self.assertIn('updated_at', base_model_str)
        self.assertIn('{', base_model_str)
        self.assertIn('}', base_model_str)
        
    def test_to_dict(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        expected_dict = {
            '__class__': 'BaseModel',
            'created_at': base_model.created_at.isoformat(),
            'updated_at': base_model.updated_at.isoformat()
            }
        try:
            del base_model_dict['id']
        except KeyError:
            pass
        self.assertDictEqual(base_model_dict, expected_dict)
        

if __name__ =='__main__':
    unittest.main()
         