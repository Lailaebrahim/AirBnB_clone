#!/usr/bin/python3
"""
Module to test BaseModel Class.
import json
"""
import os
import time
import uuid
import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
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
        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)

    def test_instantiation_without_args_with_new_attr(self):
        """Test creation with no arguments then add new attributes."""
        obj = BaseModel()
        obj.name = "laila"
        obj.age = 21
        self.assertIsNotNone(obj.id)
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)
        self.assertEqual(obj.name, "laila")
        self.assertIs(type(obj.name), str)
        self.assertEqual(obj.age, 21)
        self.assertIs(type(obj.age), int)

    def test_instantiation_with_args(self):
        """Test creation with dictionary as argument"""
        dic = {}
        dic["id"] = str(uuid.uuid4())
        dic["created_at"] = datetime.now()
        dic["updated_at"] = datetime.now()
        obj = BaseModel(dic)
        self.assertIsNotNone(obj.id)
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)

    def test_instantiation_with_args_with_new_attr(self):
        """Test creation with dictionary and test new attributes."""
        dic = {}
        dic["id"] = str(uuid.uuid4())
        dic["created_at"] = datetime.now()
        dic["updated_at"] = datetime.now()
        obj = BaseModel(dic)
        obj.name = "laila"
        obj.age = 21
        self.assertIsNotNone(obj.id)
        self.assertRegex(obj.id, '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)
        self.assertEqual(obj.name, "laila")
        self.assertIs(type(obj.name), str)
        self.assertEqual(obj.age, 21)
        self.assertIs(type(obj.age), int)

    def test_instantiation_with_empty_args(self):
        """Test creation with empty dictionary."""
        obj = BaseModel({})
        self.assertIsNotNone(obj.id)
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)

    def test_instantiation_with_None_args(self):
        """Test creation with None dictionary."""
        obj = BaseModel(None)
        self.assertNotIn(None, obj.__dict__.values())
        self.assertIsNotNone(obj.id)
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)

    def test_instantiation_with_args_none(self):
        """Test None dictionary."""
        n = {None: None}
        with self.assertRaises(TypeError):
            obj = BaseModel(**n)

    def test_str_representation(self):
        """Test string representation of BaseModel."""
        obj = BaseModel(id="456", created_at="2023-01-01T00:00:00",
                        updated_at="2023-01-01T01:00:00")
        expected_str = ("[BaseModel] (456) {'id': '456', "
                        "'created_at': datetime.datetime(2023, 1, 1, 0, 0), "
                        "'updated_at': datetime.datetime(2023, 1, 1, 1, 0)}")
        self.assertEqual(str(obj), expected_str)

    def test_to_dict(self):
        """Test serialization to a dictionary."""
        obj = BaseModel(id="789", created_at="2023-01-01T00:00:00",
                        updated_at="2023-01-01T01:00:00")
        obj.name = "laila"
        obj.age = 21
        expected_dict = {
            'id': '789',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-01T01:00:00',
            '__class__': 'BaseModel',
            'name': 'laila',
            'age': 21
        }
        self.assertEqual(obj.to_dict(), expected_dict)

    def test_return_to_ict(self):
        """Test Values returned from to_dict """
        obj = BaseModel()
        dic_obj = obj.to_dict()
        self.assertEqual(dic_obj["__class__"], "BaseModel")
        self.assertEqual(type(dic_obj["created_at"]), str)
        self.assertEqual(type(dic_obj["updated_at"]), str)
        self.assertEqual(dic_obj["updated_at"], obj.updated_at.isoformat())
        self.assertEqual(dic_obj["created_at"], obj.created_at.isoformat())

    def test_to_dict_with_dict(self):
        obj = BaseModel()
        self.assertNotEqual(obj.to_dict(), obj.__dict__)

    def test_save(self):
        """Test saving tto json file."""
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        time.sleep(1e-4)
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_two_save(self):
        """Test saving to json file."""
        obj = BaseModel()
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
        obj = BaseModel()
        obj.save()
        obj_id = "BaseModel." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(obj_id, f.read())

    def test_save_with_arg(self):
        obj = BaseModel()
        with self.assertRaises(TypeError):
            obj.save(None)

    def test_diff_attr(self):
        """Test different id, created_at time, updated_at time of two objs
        two created with an argument."""
        obj1 = BaseModel()
        time.sleep(1e-4)
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertNotEqual(obj1.created_at, obj2.created_at)
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)

    def test_diff_attr_with_args(self):
        """Test different id, created_at time, updated_at time of two objs
        one created with argument and one with an argument."""
        obj1 = BaseModel()
        obj2 = BaseModel(id="456", created_at="2023-01-01T00:00:00",
                         updated_at="2023-01-01T01:00:00")
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertNotEqual(obj1.created_at, obj2.created_at)
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)


if __name__ == '__main__':
    unittest.main()