#!/usr/bin/python3
"""
A Module to represent the Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    A Module to represent the user object
    That inherits all the attributes & methods of BaseModel class
    And define public class attributes specific to the Amenity obj.
    """

    name = ""
