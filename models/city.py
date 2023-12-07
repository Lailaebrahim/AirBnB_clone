#!/usr/bin/python3
"""
A Module to represent the City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A Module to represent the user object
    That inherits all the attributes & methods of BaseModel class
    And define public class attributes specific to the City obj.
    """

    name = ""
