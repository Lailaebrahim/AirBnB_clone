#!/usr/bin/python3
"""
A Module that handle the Storage of the project which is a File Storage
It handles: serialization/deserialization of objects
            Storing new objects
"""
import json
import os


class FileStorage:
    """
    A Class to Represent the storage that will be used in this project
    It has Two Private class attributes:
    __file_path: string - path to the JSON file
    __objects: dictionary - store all objs, key will be in form <class name>.id
    """

    __file_path = "file.json"
    __object = {}

    def all(self):
        """
        A Method to return the dictionary __objects
        :return: returns the dictionary __objects
        """
        return FileStorage.__object

    def new(self, obj):
        """
        A Method Adds to .__object a new object
        :param obj: New Objected created
        :return: No return
        """
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__object[key] = obj

    def save(self):
        """
        A Method that saves all the __objects to a json file:
        iterate over all the key/value pairs of __objects
        where each value represent an object
        So each obj is converted into a dictionary using to_dict()
        Then added to a key/value dictionary where each value is the
        dictionary representation of the obj referred to by its key
        then using json.dump to store it in a json file as a json string
        :return:
        """
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as json_file:
            dic = {}
            for key, value in FileStorage.__object.items():
                dic[key] = value.to_dict()
            json.dump(dic, json_file)

    def classes(self):
        """
        A Method to  return a dictionary of all the project classes
        and their references.
       :return: dict of all the project classes and their references
       """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """
        A Method to reload data from file storage.
        If path in __file_path refer to a file and exists
        it opens it in read mode and deserialize the data stored
        in the file in form of json string
        (it was a dict each value is the dict representation of an obj)
        then we create an instance of each obj of class type defined in
        value of key:__class__ in dict representation by referencing class
        giving it it's dict representation as an argument
        (corresponds to **kwargs)
     :return: No return
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                obj_dic = json.load(file)
                for key, value in obj_dic.items():
                    obj_dic[key] = self.classes()[value["__class__"]](**value)
                FileStorage.__objects = obj_dic

        else:
            return
