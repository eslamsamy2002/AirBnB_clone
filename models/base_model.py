#!/usr/bin/python3
"""This is the base model."""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Instance Constructor.

        Args:
            id (str): Unique identifier.
            created_at (datetime): Date created at.
            updated_at (datetime): Date updated at.
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(
                        self, k, datetime.fromisoformat(v) if k.endswith("_at") else v
                    )

    def __str__(self):
        """__str__.

        Return string representation.
        """
        class_name = self.__class__.__name__
        attributes = ", ".join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"[{class_name}] ({self.id}) {attributes}"

    def save(self):
        """Save.

        Update atr updated_at.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """To_dict.

        Returns:
            dict: Dictionary representation.
        """
        my_class_dict = self.__dict__.copy()
        my_class_dict["__class__"] = self.__class__.__name__
        my_class_dict["updated_at"] = self.updated_at.isoformat()
        my_class_dict["created_at"] = self.created_at.isoformat()
        return my_class_dict


if __name__ == "__main__":
    """Example usage in the __main__ block"""
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89

    print("Original Instance:")
    print(my_model)

    """Convert to dictionary and back to a new instance"""
    my_model_dict = my_model.to_dict()
    my_new_model = BaseModel(**my_model_dict)

    print("\nNew Instance:")
    print(my_new_model)
    print("\nInstances are the same:", my_model is my_new_model)
