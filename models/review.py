#!/usr/bin/python3
"""review model."""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class."""

    place_id = ""  # Place.id
    user_id = ""  # User.id
    text = ""

    def __init__(self, *args, **kwargs):
        """Instance Constructor.

        args
        name : string review email
        """

        super().__init__(*args, **kwargs)
