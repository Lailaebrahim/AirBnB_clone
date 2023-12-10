#!/usr/bin/python3
"""
Module to test City Class.
"""
import os
import time
import uuid
import unittest
from datetime import datetime
from models import storage
from models.city import City


class TestCityModel(unittest.TestCase):
    """Test Case to test BaseModel"""

    def setUp(self):
        """Ensure storage is empty before each test"""
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """Clean up storage after each test"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instantiation_without_args(self):
        """Test creation with no arguments."""
        obj = City()
        self.assertIsNotNone(obj.id)
        self.assertRegex(obj.id, '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)

    def test_instantiation_without_args_with_new_attr(self):
        """Test creation with no arguments then add new attributes."""
        obj = City()
        obj.name = "Paris"
        self.assertIsNotNone(obj.id)
        self.assertIs(type(obj.id), str)
        self.assertRegex(obj.id, '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)
        self.assertEqual(obj.name, "Paris")
        self.assertIs(type(obj.name), str)

    def test_instantiation_with_args(self):
        """Test creation with dictionary as argument"""
        dic = {}
        dic["id"] = str(uuid.uuid4())
        dic["created_at"] = datetime.now()
        dic["updated_at"] = datetime.now()
        obj = City(dic)
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
        obj = City(dic)
        obj.name = "Paris"
        obj.email = "laila@gmail.com"
        self.assertIsNotNone(obj.id)
        self.assertRegex(obj.id, '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)
        self.assertEqual(obj.name, "Paris")
        self.assertIs(type(obj.name), str)
        self.assertEqual(obj.email, "laila@gmail.com")
        self.assertIs(type(obj.email), str)

    def test_instantiation_with_wrong_args(self):
        """test instantiation with wrong type args."""
        obj = City()
        cpy = obj.to_dict()
        cpy.update({1: 2})
        with self.assertRaises(TypeError):
            new = City(**cpy)

    def test_instantiation_with_empty_args(self):
        """Test creation with empty dictionary."""
        obj = City({})
        self.assertIsNotNone(obj.id)
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)

    def test_instantiation_with_None_args(self):
        """Test creation with None dictionary."""
        obj = City(None)
        self.assertNotIn(None, obj.__dict__.values())
        self.assertIsNotNone(obj.id)
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)

    def test_instantiation_with_args_none(self):
        """Test None dictionary."""
        n = {None: None}
        with self.assertRaises(TypeError):
            obj = City(**n)

    def test_str_representation(self):
        """Test string representation of BaseModel."""
        obj = City(id="456", created_at="2023-01-01T00:00:00",
                   updated_at="2023-01-01T01:00:00")
        expected_str = ("[City] (456) {'id': '456', "
                        "'created_at': datetime.datetime(2023, 1, 1, 0, 0), "
                        "'updated_at': datetime.datetime(2023, 1, 1, 1, 0)}")
        self.assertEqual(str(obj), expected_str)

    def test_to_dict(self):
        """Test serialization to a dictionary."""
        obj = City(id="789", created_at="2023-01-01T00:00:00",
                   updated_at="2023-01-01T01:00:00")
        obj.name = "Paris"
        obj.email = "laila@gmail.com"
        expected_dict = {
            'id': '789',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-01T01:00:00',
            '__class__': 'City',
            'name': 'Paris',
            'email': "laila@gmail.com"
        }
        self.assertEqual(obj.to_dict(), expected_dict)

    def test_return_to_dict(self):
        """Test Values returned from to_dict """
        obj = City()
        dic_obj = obj.to_dict()
        self.assertEqual(dic_obj["__class__"], "City")
        self.assertEqual(type(dic_obj["created_at"]), str)
        self.assertEqual(type(dic_obj["updated_at"]), str)
        self.assertEqual(dic_obj["updated_at"], obj.updated_at.isoformat())
        self.assertEqual(dic_obj["created_at"], obj.created_at.isoformat())

    def test_to_dict_with_dict(self):
        """Test to dict method."""
        obj = City()
        self.assertNotEqual(obj.to_dict(), obj.__dict__)

    def test_save(self):
        """Test saving to json file."""
        obj = City()
        initial_updated_at = obj.updated_at
        time.sleep(1e-4)
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_two_save(self):
        """Test saving to json file."""
        obj = City()
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
        """test that save method updates the file"""
        obj = City()
        obj.save()
        obj_id = "City." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(obj_id, f.read())

    def test_save_with_arg(self):
        """test save method with arguments"""
        obj = City()
        with self.assertRaises(TypeError):
            obj.save(None)

    def test_diff_attr(self):
        """Test different id, created_at time, updated_at time of two objs
        two created with an argument."""
        obj1 = City()
        time.sleep(1e-4)
        obj2 = City()
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertNotEqual(obj1.created_at, obj2.created_at)
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)

    def test_diff_attr_with_args(self):
        """Test different id, created_at time, updated_at time of two objs
        one created with argument and one with an argument."""
        obj1 = City()
        obj2 = City(id="456", created_at="2023-01-01T00:00:00",
                    updated_at="2023-01-01T01:00:00")
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertNotEqual(obj1.created_at, obj2.created_at)
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)
