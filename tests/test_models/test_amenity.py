#!/usr/bin/python3
"""Unittest for base model
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestConstructor(unittest.TestCase):
    """
    test class for the max_integer() function.
    """
    amenity = Amenity()
    amenity.name = "Ali"
    amenity.id = "123-123-123"

    def test_default_values(self):
        """test default value"""

        a = Amenity()
        self.assertEqual(a.name, "")

    def test_create_instance_without_kwargs(self):
        """
        create an instance of class without kwargs
        """
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

        self.assertEqual(self.amenity.name, "Ali")
        self.assertEqual(self.amenity.id, "123-123-123")

    def test_create_instance_with_kwargs(self):
        """
        create an instance of class using kwargs
        """
        my_amenity_json = self.amenity.to_dict()
        new_amenity = Amenity(**my_amenity_json)
        self.assertIsInstance(new_amenity, Amenity)
        self.assertIsInstance(new_amenity.id, str)
        self.assertIsInstance(new_amenity.created_at, datetime)
        self.assertIsInstance(new_amenity.updated_at, datetime)
        self.assertEqual(new_amenity.name, "Ali")
        self.assertEqual(new_amenity.id, "123-123-123")
        self.assertNotEqual(new_amenity, self.amenity)
        self.assertDictEqual(new_amenity.__dict__, self.amenity.__dict__)

    def test_to_dict(self):
        """
            test to_dict class method
        """
        to_dict_returned_dict = self.amenity.to_dict()
        expected_dic = self.amenity.__dict__.copy()
        expected_dic["__class__"] = self.amenity.__class__.__name__
        expected_dic["updated_at"] = self.amenity.updated_at.isoformat()
        expected_dic["created_at"] = self.amenity.created_at.isoformat()
        self.assertDictEqual(expected_dic, to_dict_returned_dict)

    def test_save(self):
        """"
            test save class method
        """
        before_update_time = self.amenity.updated_at
        self.amenity.name = "Emad"
        self.amenity.save()
        after_update_time = self.amenity.updated_at
        self.assertNotEqual(before_update_time, after_update_time)
        # all_objects = storage.all()
        # new_number = all_objects[self.amenity.__class__.__name__ +
        #                          "." + self.amenity.id]["name"]
        # self.assertEqual(new_number, "Emad")

    def test_str(self):
        """
            test str method

            check for string representaion
        """
        n = self.amenity.__class__.__name__

        expected_str = f"[{n}] ({self.amenity.id}) <{self.amenity.__dict__}>"
        self.assertEqual(self.amenity.__str__(), expected_str)
