#!/usr/bin/python3
"""
Module to test BaseModel Class.
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

    def test_id_is_public_attr(self):
        """Test id is public attribute"""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_attr(self):
        """Test created_at is public attribute"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_attr(self):
        """Test updated_at is public attribute"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_instantiation_without_args(self):
        """Test creation with no arguments."""
        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)
        self.assertEqual(BaseModel, type(obj))

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

    def test_instantiation_with_wrong_args(self):
        """test instantiation with wrong type args."""
        obj = BaseModel()
        cpy = obj.to_dict()
        cpy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**cpy)

    def test_instantiation_with_empty_args(self):
        """Test creation with empty dictionary."""
        obj = BaseModel({})
        self.assertIsNotNone(obj.id)
        self.assertRegex(obj.id, '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
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

    def test_to_dict_type(self):
        """test return type of to_dict method."""
        obj = BaseModel()
        self.assertTrue(dict, type(obj.to_dict()))

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
        self.assertIn("id", obj.to_dict())
        self.assertIn("created_at", obj.to_dict())
        self.assertIn("updated_at", obj.to_dict())
        self.assertIn("__class__", obj.to_dict())

    def test_to_dict_with_new_attr(self):
        """Test to dict and new added attributes."""
        obj = BaseModel()
        obj.name = "laila"
        obj.age = 21
        self.assertIn("name", obj.to_dict())
        self.assertIn("age", obj.to_dict())

    def test_return_to_dict(self):
        """Test Values returned from to_dict """
        obj = BaseModel()
        dic_obj = obj.to_dict()
        self.assertEqual(dic_obj["__class__"], "BaseModel")
        self.assertEqual(type(dic_obj["created_at"]), str)
        self.assertEqual(type(dic_obj["updated_at"]), str)
        self.assertEqual(dic_obj["updated_at"], obj.updated_at.isoformat())
        self.assertEqual(dic_obj["created_at"], obj.created_at.isoformat())

    def test_to_dict_with_dict(self):
        """test to dict method"""
        obj = BaseModel()
        self.assertNotEqual(obj.to_dict(), obj.__dict__)

    def test_to_dict_with_None_arg(self):
        """test to dict with None arg."""
        obj = BaseModel()
        with self.assertRaises(TypeError):
            obj.to_dict(None)

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
        self.assertLess(initial_updated_at, obj.updated_at)
        second_update_at = obj.updated_at
        time.sleep(1e-4)
        obj.save()
        self.assertNotEqual(second_update_at, obj.updated_at)
        self.assertNotEqual(second_update_at, initial_updated_at)
        self.assertLess(initial_updated_at, second_update_at)

    def test_save_updates_file(self):
        """test that save method updates the file"""
        obj = BaseModel()
        obj.save()
        obj_id = "BaseModel." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(obj_id, f.read())

    def test_save_with_arg(self):
        """test save method with arguments"""
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
