#!/usr/bin/python3
"""FileStorage class for storing and retrieving data."""
import datetime
import json
import os

class FileStorage:
    """Stores and retrieves data."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage."""
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects to a JSON file."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def classes(self):
        """Returns valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User


        classes = {"BaseModel": BaseModel,
                   "User": User}
        return classes

    def reload(self):
        """Reloads stored objects from JSON file."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def attributes(self):
        """Returns valid attributes and their types for each class."""
        attributes = {
            "BaseModel": {"id": str,
                          "created_at": datetime.datetime,
                          "updated_at": datetime.datetime},
            "User": {"email": str,
                     "password": str,
                     "first_name": str,
                     "last_name": str},
            
        }
        return attributes
