#!/usr/bin/python3
"""

"""
import uuid
from datetime import datetime


class BaseModel:
    def__init__(self):
        self.id = str(uuid.uuid4())
        
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        
    def save(self):
        """
        """
        self.updated_at = datetime.utcnow()
        
    def to_dict(self):
        """
        
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
