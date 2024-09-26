#!/usr/bin/python3
"""
Create a base model that contains common
attributes for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """Save and update date of an object"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        returns a dictionary containing
        all keys/values of __dict__ of the instanc
        """
        mydict = self.__dict__.copy()
        mydict["__class__"] = self.__class__.__name__
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()

        return mydict

    def __str__(self):
        """A method to print class name, id and its dict"""
        class_name = self.__class__.__name__
        return "[{}], ({}), {}".format(class_name, self.id, self.__dict__)
