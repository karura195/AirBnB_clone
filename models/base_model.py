#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
"""
Module BaseModel
"""
# fdate = date format
fdate = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """
    Class BaseModel that defines all common attributes/methods
    for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        This method allow the class to initialize the attributes id,
        created_at and updated_at.
        """
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    setattr(self, key, val)
                    if hasattr(self, 'created_at') and type(
                            self.created_at) is str:
                        self.created_at = datetime.strptime(
                            kwargs["created_at"], fdate)
                    if hasattr(self, 'updated_at') and type(
                            self.updated_at) is str:
                        self.updated_at = datetime.strptime(
                            kwargs["updated_at"], fdate)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        This method returns the string representation as
        [<class name>] (<self.id>) <self.__dict__>
        """
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
