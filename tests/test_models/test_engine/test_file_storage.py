#!/usr/bin/python3
"""
test module
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import os

class TestConstructor(unittest.TestCase):
    """
    test class
    """
    fs = FileStorage()

    def test_default_values(self):
        """test default value"""
        # Get the initial count of objects
        initial_count = len(self.fs.all())
        old_dict = self.fs.all().copy()
        # Create a new BaseModel instance and add it to the FileStorage
        new_base_model = BaseModel()
        self.fs.new(new_base_model)

        # Save the objects to the JSON file
        self.fs.save()

        # Reload the objects from the JSON file
        self.fs.reload()

        # Get the updated count of objects
        updated_count = len(self.fs.all())
        # Verify that the count of objects has increased by 1
        self.assertEqual(updated_count, initial_count + 1)

        # Verify that the added object is now present in the objects dictionary
        obj_key = f"BaseModel.{new_base_model.id}"
        self.assertIn(obj_key, self.fs.all())

        # Verify that the attributes of the added object match the original attributes
        reloaded_obj = self.fs.all()[obj_key]
        self.assertEqual(reloaded_obj.updated_at, new_base_model.updated_at)

        os.remove("file.json")
        new_base_model = BaseModel()
        new_base_model.save()
        self.assertTrue(os.path.exists("file.json"))
