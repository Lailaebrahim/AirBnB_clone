#!/usr/bin/python3
"""
A Module to represent the User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A Module to represent the user object
    That inherits all the attributes & methods of BaseModel class
    And define public class attributes specific to the user obj.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
