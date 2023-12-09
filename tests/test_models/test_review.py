#!/usr/bin/python3
"""
Module to test Review Class.
"""
import os
import time
import uuid
import unittest
from datetime import datetime
from models import storage
from models.review import Review
from models.user import User
from models.place import Place


class TestReviewModel(unittest.TestCase):
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
        obj = Review()
        self.assertIsNotNone(obj.id)
        self.assertRegex(obj.id, '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)

    def test_instantiation_without_args_with_new_attr(self):
        """Test creation with no arguments then add new attributes."""
        obj = Review()
        p = Place(id="222", created_at="2023-12-01T00:00:00",
                  updated_at="2023-01-01T01:00:00")
        us = User(id="111", created_at="2023-01-01T00:00:00",
                  updated_at="2023-01-01T01:00:00")
        obj.place_id = p.id
        obj.user_id = us.id
        obj.text = "Good"
        self.assertIsNotNone(obj.id)
        self.assertIs(type(obj.id), str)
        self.assertRegex(obj.id, '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)
        self.assertEqual(obj.text, "Good")
        self.assertIs(type(obj.text), str)
        self.assertEqual(obj.place_id, "222")
        self.assertIs(type(obj.place_id), str)
        self.assertEqual(obj.user_id, "111")
        self.assertIs(type(obj.user_id), str)
        self.assertEqual(obj.text, "Good")
        self.assertIs(type(obj.text), str)

    def test_instantiation_with_args(self):
        """Test creation with dictionary as argument"""
        dic = {}
        dic["id"] = str(uuid.uuid4())
        dic["created_at"] = datetime.now()
        dic["updated_at"] = datetime.now()
        obj = Review(dic)
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
        obj = Review(dic)
        p = Place(id="222", created_at="2023-12-01T00:00:00",
                  updated_at="2023-01-01T01:00:00")
        us = User(id="111", created_at="2023-01-01T00:00:00",
                  updated_at="2023-01-01T01:00:00")
        obj.place_id = p.id
        obj.user_id = us.id
        obj.text = "Good"
        self.assertIsNotNone(obj.id)
        self.assertRegex(obj.id, '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)
        self.assertEqual(obj.text, "Good")
        self.assertIs(type(obj.text), str)
        self.assertEqual(obj.place_id, "222")
        self.assertIs(type(obj.place_id), str)
        self.assertEqual(obj.user_id, "111")
        self.assertIs(type(obj.user_id), str)
        self.assertEqual(obj.text, "Good")
        self.assertIs(type(obj.text), str)

    def test_instantiation_with_empty_args(self):
        """Test creation with empty dictionary."""
        obj = Review({})
        self.assertIsNotNone(obj.id)
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)

    def test_instantiation_with_None_args(self):
        """Test creation with None dictionary."""
        obj = Review(None)
        self.assertNotIn(None, obj.__dict__.values())
        self.assertIsNotNone(obj.id)
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)

    def test_instantiation_with_args_none(self):
        """Test None dictionary."""
        n = {None: None}
        with self.assertRaises(TypeError):
            obj = Review(**n)

    def test_str_representation(self):
        """Test string representation of BaseModel."""
        obj = Review(id="456", created_at="2023-01-01T00:00:00",
                     updated_at="2023-01-01T01:00:00")
        expected_str = ("[Review] (456) {'id': '456', "
                        "'created_at': datetime.datetime(2023, 1, 1, 0, 0), "
                        "'updated_at': datetime.datetime(2023, 1, 1, 1, 0)}")
        self.assertEqual(str(obj), expected_str)

    def test_to_dict(self):
        """Test serialization to a dictionary."""
        obj = Review(id="789", created_at="2023-01-01T00:00:00",
                     updated_at="2023-01-01T01:00:00")
        p = Place(id="222", created_at="2023-12-01T00:00:00",
                  updated_at="2023-01-01T01:00:00")
        us = User(id="111", created_at="2023-01-01T00:00:00",
                  updated_at="2023-01-01T01:00:00")
        obj.place_id = p.id
        obj.user_id = us.id
        obj.text = "Good"
        expected_dict = {
            'id': '789',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-01T01:00:00',
            '__class__': 'Review',
            'place_id': '222',
            'user_id': '111',
            'text': "Good"
        }
        self.assertEqual(obj.to_dict(), expected_dict)

    def test_return_to_dict(self):
        """Test Values returned from to_dict """
        obj = Review()
        dic_obj = obj.to_dict()
        self.assertEqual(dic_obj["__class__"], "Review")
        self.assertEqual(type(dic_obj["created_at"]), str)
        self.assertEqual(type(dic_obj["updated_at"]), str)
        self.assertEqual(dic_obj["updated_at"], obj.updated_at.isoformat())
        self.assertEqual(dic_obj["created_at"], obj.created_at.isoformat())

    def test_to_dict_with_dict(self):
        obj = Review()
        self.assertNotEqual(obj.to_dict(), obj.__dict__)

    def test_save(self):
        """Test saving to json file."""
        obj = Review()
        initial_updated_at = obj.updated_at
        time.sleep(1e-4)
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_two_save(self):
        """Test saving to json file."""
        obj = Review()
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
        obj = Review()
        obj.save()
        obj_id = "Review." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(obj_id, f.read())

    def test_save_with_arg(self):
        obj = Review()
        with self.assertRaises(TypeError):
            obj.save(None)

    def test_diff_attr(self):
        """Test different id, created_at time, updated_at time of two objs
        two created with an argument."""
        obj1 = Review()
        time.sleep(1e-4)
        obj2 = Review()
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertNotEqual(obj1.created_at, obj2.created_at)
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)

    def test_diff_attr_with_args(self):
        """Test different id, created_at time, updated_at time of two objs
        one created with argument and one with an argument."""
        obj1 = Review()
        obj2 = Review(id="456", created_at="2023-01-01T00:00:00",
                      updated_at="2023-01-01T01:00:00")
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertNotEqual(obj1.created_at, obj2.created_at)
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)


if __name__ == '__main__':
    unittest.main()
