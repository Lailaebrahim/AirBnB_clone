#!/usr/bin/python3
"""
Module to test Place Class.
"""
import os
import time
import uuid
import unittest
from datetime import datetime
from models import storage
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity


class TestPlaceModel(unittest.TestCase):
    """Test Case to test BaseModel"""

    def setUp(self):
        # Ensure storage is empty before each test
        storage._FileStorage__objects = {}

    def tearDown(self):
        # Clean up storage after each test
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instantiation_without_args(self):
        """Test creation with no arguments."""
        obj = Place()
        self.assertIsNotNone(obj.id)
        self.assertRegex(obj.id, '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)

    def test_instantiation_without_args_with_new_attr(self):
        """Test creation with no arguments then add new attributes."""
        obj = Place()
        city = City()
        us = User()
        am = Amenity()
        obj.city_id = city.id
        obj.user_id = us.id
        obj.name = "Laila"
        obj.description = "Good Place"
        obj.number_rooms = 1
        obj.number_bathrooms = 1
        obj.max_guest = 2
        obj.price_by_night = 100
        obj.latitude = 1.1
        obj.longitude = 2.2
        obj.amenity_ids = [am.id, ]
        self.assertIsNotNone(obj.id)
        self.assertIs(type(obj.id), str)
        self.assertRegex(obj.id, '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)
        self.assertEqual(obj.name, "Laila")
        self.assertIs(type(obj.name), str)
        self.assertEqual(obj.city_id, city.id)
        self.assertIs(type(obj.city_id), str)
        self.assertEqual(obj.user_id, us.id)
        self.assertIs(type(obj.user_id), str)
        self.assertEqual(obj.description, "Good Place")
        self.assertIs(type(obj.description), str)
        self.assertEqual(obj.number_rooms, 1)
        self.assertIs(type(obj.number_rooms), int)
        self.assertEqual(obj.number_bathrooms, 1)
        self.assertIs(type(obj.number_bathrooms), int)
        self.assertEqual(obj.max_guest, 2)
        self.assertIs(type(obj.max_guest), int)
        self.assertEqual(obj.price_by_night, 100)
        self.assertIs(type(obj.price_by_night), int)
        self.assertEqual(obj.latitude, 1.1)
        self.assertIs(type(obj.latitude), float)
        self.assertEqual(obj.longitude, 2.2)
        self.assertIs(type(obj.longitude), float)
        self.assertEqual(obj.amenity_ids, [am.id, ])
        self.assertIs(type(obj.amenity_ids), list)

    def test_instantiation_with_args(self):
        """Test creation with dictionary as argument"""
        dic = {}
        dic["id"] = str(uuid.uuid4())
        dic["created_at"] = datetime.now()
        dic["updated_at"] = datetime.now()
        obj = Place(dic)
        self.assertIsNotNone(obj.id)
        self.assertRegex(obj.id, '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)

    def test_instantiation_with_args_with_new_attr(self):
        """Test creation with dictionary and test new attributes."""
        dic = {}
        dic["id"] = str(uuid.uuid4())
        dic["created_at"] = datetime.now()
        dic["updated_at"] = datetime.now()
        obj = Place(dic)
        obj.name = "Room1"
        obj.max_guest = 2
        obj.email = "laila@gmail.com"
        self.assertIsNotNone(obj.id)
        self.assertRegex(obj.id, '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)
        self.assertEqual(obj.name, "Room1")
        self.assertIs(type(obj.name), str)
        self.assertEqual(obj.email, "laila@gmail.com")
        self.assertIs(type(obj.email), str)
        self.assertEqual(obj.max_guest, 2)
        self.assertIs(type(obj.max_guest), int)

    def test_instantiation_with_empty_args(self):
        """Test creation with empty dictionary."""
        obj = Place({})
        self.assertIsNotNone(obj.id)
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)

    def test_instantiation_with_None_args(self):
        """Test creation with None dictionary."""
        obj = Place(None)
        self.assertNotIn(None, obj.__dict__.values())
        self.assertIsNotNone(obj.id)
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)

    def test_instantiation_with_args_none(self):
        """Test None dictionary."""
        n = {None: None}
        with self.assertRaises(TypeError):
            obj = Place(**n)

    def test_str_representation(self):
        """Test string representation of BaseModel."""
        obj = Place(id="456", created_at="2023-01-01T00:00:00",
                    updated_at="2023-01-01T01:00:00")
        expected_str = ("[Place] (456) {'id': '456', "
                        "'created_at': datetime.datetime(2023, 1, 1, 0, 0), "
                        "'updated_at': datetime.datetime(2023, 1, 1, 1, 0)}")
        self.assertEqual(str(obj), expected_str)
        obj = Place(id="123", created_at="2023-12-01T00:00:00",
                    updated_at="2023-01-01T01:00:00", name="Laila")
        expected_str = ("[Place] (123) {'id': '123', "
                        "'created_at': datetime.datetime(2023, 12, 1, 0, 0), "
                        "'updated_at': datetime.datetime(2023, 1, 1, 1, 0), "
                        "'name': 'Laila'}")
        self.assertEqual(str(obj), expected_str)

    def test_to_dict(self):
        """Test serialization to a dictionary."""
        obj = Place(id="789", created_at="2023-01-01T00:00:00",
                    updated_at="2023-01-01T01:00:00")
        obj.name = "Room1"
        obj.email = "laila@gmail.com"
        obj.number_rooms = 1
        obj.latitude = 1.1
        am1 = Amenity(id="111", created_at="2023-01-01T00:00:00",
                      updated_at="2023-01-01T01:00:00")
        am2 = Amenity(id="222", created_at="2023-01-01T00:00:00",
                      updated_at="2023-01-01T01:00:00")
        obj.amenity_ids = [am1.id, am2.id]
        expected_dict = {
            'id': '789',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-01T01:00:00',
            '__class__': 'Place',
            'name': 'Room1',
            'email': 'laila@gmail.com',
            'number_rooms': 1,
            'latitude': 1.1,
            'amenity_ids': ['111', '222']
        }
        self.assertEqual(obj.to_dict(), expected_dict)

    def test_return_to_dict(self):
        """Test Values returned from to_dict """
        obj = Place()
        dic_obj = obj.to_dict()
        self.assertEqual(dic_obj["__class__"], "Place")
        self.assertEqual(type(dic_obj["created_at"]), str)
        self.assertEqual(type(dic_obj["updated_at"]), str)
        self.assertEqual(dic_obj["updated_at"], obj.updated_at.isoformat())
        self.assertEqual(dic_obj["created_at"], obj.created_at.isoformat())

    def test_to_dict_with_dict(self):
        obj = Place()
        self.assertNotEqual(obj.to_dict(), obj.__dict__)

    def test_save(self):
        """Test saving to json file."""
        obj = Place()
        initial_updated_at = obj.updated_at
        time.sleep(1e-4)
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_two_save(self):
        """Test saving to json file."""
        obj = Place()
        initial_updated_at = obj.updated_at
        time.sleep(1e-4)
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)
        second_update_at = obj.updated_at
        time.sleep(1e-4)
        obj.save()
        self.assertNotEqual(second_update_at, obj.updated_at)
        self.assertNotEqual(second_update_at, initial_updated_at)

    def test_save_updates_file(self):
        obj = Place()
        obj.save()
        obj_id = "Place." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(obj_id, f.read())

    def test_save_with_arg(self):
        us = Place()
        with self.assertRaises(TypeError):
            us.save(None)

    def test_diff_attr(self):
        """Test different id, created_at time, updated_at time of two objs
        two created with an argument."""
        obj1 = Place()
        time.sleep(1e-4)
        obj2 = Place()
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertNotEqual(obj1.created_at, obj2.created_at)
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)

    def test_diff_attr_with_args(self):
        """Test different id, created_at time, updated_at time of two objs
        one created with argument and one with an argument."""
        obj1 = Place()
        obj2 = Place(id="456", created_at="2023-01-01T00:00:00",
                     updated_at="2023-01-01T01:00:00")
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertNotEqual(obj1.created_at, obj2.created_at)
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)


if __name__ == '__main__':
    unittest.main()
