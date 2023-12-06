#!/usr/bin/python3
"""
A Module to represent the Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    A Module to represent the user object
    That inherits all the attributes & methods of BaseModel class
    And define public class attributes specific to the Place obj.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
