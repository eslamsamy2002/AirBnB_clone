#!/usr/bin/python3
"""Unittest for base model
"""
import unittest
from models.city import City
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestConstructor(unittest.TestCase):
    """
    test class for the max_integer() function.
    """
    city = City()
    city.name = "Ali"
    city.id = "123-123-123"

    def test_default_values(self):
        """test default value"""

        c = City()
        self.assertEqual(c.name, "")
        self.assertEqual(c.state_id, "")

    def test_create_instance_without_kwargs(self):
        """
        create an instance of class without kwargs
        """
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)
        self.assertEqual(self.city.name, "Ali")
        self.assertEqual(self.city.id, "123-123-123")

    def test_create_instance_with_kwargs(self):
        """
        create an instance of class using kwargs
        """
        my_city_json = self.city.to_dict()
        new_city = City(**my_city_json)
        self.assertIsInstance(new_city, City)
        self.assertIsInstance(new_city.id, str)
        self.assertIsInstance(new_city.created_at, datetime)
        self.assertIsInstance(new_city.updated_at, datetime)
        self.assertEqual(new_city.name, "Ali")
        self.assertEqual(new_city.id, "123-123-123")
        self.assertNotEqual(new_city, self.city)
        self.assertDictEqual(new_city.__dict__, self.city.__dict__)
        new_city.state_id = "123-122"
        new_city.name = "Emad"
        new_city.save()
        self.assertEqual(new_city.state_id, "123-122")
        self.assertEqual(new_city.name, "Emad")
        self.assertEqual(new_city.__dict__["name"], "Emad")
        self.assertEqual(new_city.__dict__["state_id"], "123-122")

    def test_to_dict(self):
        """
            test to_dict class method
        """
        to_dict_returned_dict = self.city.to_dict()
        expected_dic = self.city.__dict__.copy()
        expected_dic["__class__"] = self.city.__class__.__name__
        expected_dic["updated_at"] = self.city.updated_at.isoformat()
        expected_dic["created_at"] = self.city.created_at.isoformat()
        self.assertDictEqual(expected_dic, to_dict_returned_dict)

    def test_save(self):
        """"
            test save class method
        """
        before_update_time = self.city.updated_at
        self.city.name = "Body"
        self.city.save()
        after_update_time = self.city.updated_at
        self.assertNotEqual(before_update_time, after_update_time)
        # all_objects = storage.all()
        # new_number = all_objects[self.city.__class__.__name__ +
        #                          "." + self.city.id]["name"]
        # self.assertEqual(new_number, "Body")

    def test_str(self):
        """
            test str method

            check for string representaion
        """
        n = self.city.__class__.__name__
        expected_str = f"[{n}] ({self.city.id}) <{self.city.__dict__}>"
        self.assertEqual(self.city.__str__(), expected_str)
