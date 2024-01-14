#!/usr/bin/python3
"""Unittest for base model
"""
import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestConstructor(unittest.TestCase):
    """
    test class for the max_integer() function.
    """
    user = User()
    user.email = "Emad@Alx.com"
    user.password = "EL0mda"
    user.first_name = "Emad"
    user.last_name = "Anwer"

    def test_default_values(self):
        """test default value"""

        u = User()
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")
    def test_create_instance_without_kwargs(self):
        """
        create an instance of class without kwargs
        """
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user, BaseModel)
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
        self.assertEqual(self.user.email, "Emad@Alx.com")
        self.assertEqual(self.user.password, "EL0mda")
        self.assertEqual(self.user.first_name, "Emad")
        self.assertEqual(self.user.last_name, "Anwer")

    def test_create_instance_with_kwargs(self):
        """
        create an instance of class using kwargs
        """
        user_data = {
            "id": "user-123",
            "email": "Ali@Alx.com",
            "password": "new_password",
            "first_name": "Ali",
            "last_name": "Anwer",
            "created_at": "2023-08-11T23:00:25.886465",
            "updated_at": "2023-08-11T23:00:25.886466"
        }

        new_user = User(**user_data)

        self.assertIsInstance(new_user, User)
        self.assertIsInstance(new_user, BaseModel)
        self.assertIsInstance(new_user.id, str)
        self.assertIsInstance(new_user.created_at, datetime)
        self.assertIsInstance(new_user.updated_at, datetime)
        self.assertIsInstance(new_user.email, str)
        self.assertIsInstance(new_user.password, str)
        self.assertIsInstance(new_user.first_name, str)
        self.assertIsInstance(new_user.last_name, str)

        self.assertEqual(new_user.id, "user-123")
        self.assertEqual(new_user.email, "Ali@Alx.com")
        self.assertEqual(new_user.password, "new_password")
        self.assertEqual(new_user.first_name, "Ali")
        self.assertEqual(new_user.last_name, "Anwer")

    def test_to_dict(self):
        """
            test to_dict class method
        """
        to_dict_returned_dict = self.user.to_dict()
        expected_dict = self.user.__dict__.copy()
        expected_dict["__class__"] = self.user.__class__.__name__
        expected_dict["updated_at"] = self.user.updated_at.isoformat()
        expected_dict["created_at"] = self.user.created_at.isoformat()
        self.assertDictEqual(expected_dict, to_dict_returned_dict)

    def test_save(self):
        """"
            test save class method
        """
        before_update_time = self.user.updated_at
        self.user.email = "updated@example.com"
        self.user.save()
        after_update_time = self.user.updated_at
        self.assertNotEqual(before_update_time, after_update_time)

    def test_str(self):
        """
            test str method

            check for string representaion
        """
        n = self.user.__class__.__name__
        expected_str = f"[{n}] ({self.user.id}) <{self.user.__dict__}>"
        self.assertEqual(self.user.__str__(), expected_str)
