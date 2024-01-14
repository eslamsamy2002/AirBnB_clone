#!/usr/bin/python3
"""this is the base model."""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Instance Constructor.

        args
        id:unique identifier.
        created_at: date created at.
        updated_at: date updated at.
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "updated_at":
                        self.updated_at = datetime.fromisoformat(v)
                    elif k == "created_at":
                        self.created_at = datetime.fromisoformat(v)
                    else:
                        setattr(self, k, v)

    def __str__(self):
        """__str__.

        return string Representation.
        """
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """save.

        update atr updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """To_dict.

        Returns:
            dict: dictionary representation.
        """
        my_class_dict = self.__dict__.copy()
        my_class_dict["__class__"] = self.__class__.__name__
        my_class_dict["updated_at"] = self.updated_at.isoformat()
        my_class_dict["created_at"] = self.created_at.isoformat()
        return my_class_dict
