#!/usr/bin/python3
"""
A Module to represent the Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A Module to represent the user object
    That inherits all the attributes & methods of BaseModel class
    And define public class attributes specific to the Review obj.
    """

    place_id = ""
    user_id = ""
    text = ""
