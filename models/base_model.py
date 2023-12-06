#!/usr/bin/python3
"""
A module to define the base module for all other classes of the project
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    A class which is tha base for all the project classes
    It has all the attributes and methods that is
    common between them all.
    """

    def __init__(self, *args, **kwargs):
        """
        The constructor
        In case of a dictionary was given as an argument:
            created_at and updated_at vale is a string of
            time formatted with ISO, so we need to convert it back
            to datetime object
        :param args: A tuple of arguments.
        :param kwargs: A dictionary of key/value arguments.
        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.fromisoformat(kwargs["created_at"])
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.fromisoformat(kwargs["updated_at"])
                else:
                    self.__dict__[key] = kwargs[key]

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """
        Method to update the time of last update.
        And save the updated obj to file storage.
        :return: No return
        """
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """
        Represent the object in a human-readable way.
        :return: string representation of the object.
        """
        return f"[{type( self ).__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """
        Method to return the dictionary representation of the object
        Adding a new key/value __class__ that store the name of the class of obj
        And formatting the created_at and updated_at by ISO format for time.
        :return: A dictionary representation the object
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
