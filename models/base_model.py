#!/usr/bin/python3
"""BaseModel class that defines all common attributes/methods
for other classes"""
import uuid
import datetime
import models


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """__init__ method for BaseModel class"""

        if kwargs:
            for name, value in kwargs.items():
                if name != '__class__':
                    if name == 'created_at' or name == 'updated_at':
                        value = datetime.datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, name, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """string representation of BaseModel"""

        return ("[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at with the
        current datetime"""

        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""

        model_dict = dict(self.__dict__)
        model_dict['__class__'] = type(self).__name__
        model_dict['created_at'] = model_dict['created_at'].isoformat()
        model_dict['updated_at'] = model_dict['updated_at'].isoformat()
        return model_dict
