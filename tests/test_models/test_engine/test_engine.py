#!/usr/bin/python3
"""
Module to test File Storage.
"""
import os
import json
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestAmenityModel(unittest.TestCase):
    """Test Case to test BaseModel"""

    def setUp(self):
        """Ensure storage is empty before each test
        storage._FileStorage__objects = {}"""
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """Clean up storage after each test"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_objects_dict_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_instantiation_without_args(self):
        """Test creation with no arguments."""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_instantiation_with_args(self):
        """Test creation with arguments."""
        with self.assertRaises(TypeError):
            FileStorage(BaseModel())

    def test_instantiation_with_None_args(self):
        """Test creation with arguments."""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_File_Storage_objects_priv_attr(self):
        """Test type of private attributes."""
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_File_Storage_file_path_priv_attr(self):
        """Test type of private attributes."""
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_storage_instantiation(self):
        """Test storage_instantiation."""
        self.assertEqual(type(storage), FileStorage)

    def test_creation_file(self):
        """ File is not created on a class save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_file_creation_after_save(self):
        """ file is created after save"""
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_file_after_save_not_empty(self):
        """Test file is not empty after saving"""
        new = BaseModel()
        dict = new.to_dict()
        new.save()
        new2 = BaseModel(**dict)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_all(self):
        """Test all method."""
        new = BaseModel()
        objs = storage.all()
        self.assertIs(type(objs), dict)

    def test_all_with_args(self):
        """test all method with args"""
        with self.assertRaises(TypeError):
            storage.all(BaseModel())

    def test_all_with_None_args(self):
        """test all method with args"""
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new(self):
        """test new method"""
        obj0 = Amenity()
        obj1 = BaseModel()
        obj2 = City()
        obj3 = Place()
        obj4 = Review()
        obj5 = State()
        obj6 = User()
        storage.new(obj0)
        storage.new(obj1)
        storage.new(obj2)
        storage.new(obj3)
        storage.new(obj4)
        storage.new(obj5)
        storage.new(obj6)
        objs = storage.all()
        self.assertFalse(os.path.exists('file.json'))
        self.assertIn("Amenity." + obj0.id, objs.keys())
        self.assertIn(obj0, objs.values())
        self.assertIn("BaseModel." + obj1.id, objs.keys())
        self.assertIn(obj1, objs.values())
        self.assertIn("City." + obj2.id, objs.keys())
        self.assertIn(obj2, objs.values())
        self.assertIn("Place." + obj3.id, objs.keys())
        self.assertIn(obj3, objs.values())
        self.assertIn("Review." + obj4.id, objs.keys())
        self.assertIn(obj4, objs.values())
        self.assertIn("State." + obj5.id, objs.keys())
        self.assertIn(obj5, objs.values())
        self.assertIn("User." + obj6.id, objs.keys())
        self.assertIn(obj6, objs.values())

    def test_new_add_to_objects(self):
        """test that new adds an object to the FileStorage.__objects attr"""
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in storage.classes().items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_new_with_args(self):
        """Test new method with arguments """
        with self.assertRaises(TypeError):
            storage.new(Amenity(), BaseModel())

    def test_new_with_None_arg(self):
        """test new method with None argument"""
        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_save(self):
        """test save method."""
        obj0 = Amenity()
        obj1 = BaseModel()
        obj2 = City()
        obj3 = Place()
        obj4 = Review()
        obj5 = State()
        obj6 = User()
        storage.new(obj0)
        storage.new(obj1)
        storage.new(obj2)
        storage.new(obj3)
        storage.new(obj4)
        storage.new(obj5)
        storage.new(obj6)
        storage.save()
        self.assertTrue(os.path.exists('file.json'))
        json_string = ""
        with open(storage._FileStorage__file_path, "r") as f:
            json_string = f.read()
            self.assertIn("Amenity." + obj0.id, json_string)
            self.assertIn("BaseModel." + obj1.id, json_string)
            self.assertIn("City." + obj2.id, json_string)
            self.assertIn("Place." + obj3.id, json_string)
            self.assertIn("Review." + obj4.id, json_string)
            self.assertIn("State." + obj5.id, json_string)
            self.assertIn("User." + obj6.id, json_string)

    def test_save(self):
        """Test that save properly saves objects to file.json"""
        new_dict = {}
        for key, value in storage.classes().items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))

    def test_save_with_args(self):
        """test save method with argument."""
        with self.assertRaises(TypeError):
            storage.save(Amenity(), BaseModel())

    def test_save_with_None_arg(self):
        """test save method with one argument."""
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload(self):
        """test reload method."""
        obj0 = Amenity()
        obj1 = BaseModel()
        obj2 = City()
        obj3 = Place()
        obj4 = Review()
        obj5 = State()
        obj6 = User()
        storage.new(obj0)
        storage.new(obj1)
        storage.new(obj2)
        storage.new(obj3)
        storage.new(obj4)
        storage.new(obj5)
        storage.new(obj6)
        storage.save()
        self.assertTrue(os.path.exists('file.json'))
        storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("Amenity." + obj0.id, objs.keys())
        self.assertIn("BaseModel." + obj1.id, objs.keys())
        self.assertIn("City." + obj2.id, objs.keys())
        self.assertIn("Place." + obj3.id, objs.keys())
        self.assertIn("Review." + obj4.id, objs.keys())
        self.assertIn("State." + obj5.id, objs.keys())
        self.assertIn("User." + obj6.id, objs.keys())

    def test_reload_empty(self):
        """ test load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_reload_with_arg(self):
        """test reload method with argument."""
        with self.assertRaises(TypeError):
            storage.reload(BaseModel())

    def test_reload_with_None_arg(self):
        """test reload method with None argument."""
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_key_format(self):
        """ test Key is properly formatted """
        obj = BaseModel()
        _id = obj.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)


if __name__ == '__main__':
    unittest.main()
