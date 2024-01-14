#!usr/bin/python3

""" User model """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """init the user class"""
        super().__init__(*args, **kwargs)
