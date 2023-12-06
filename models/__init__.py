#!/usr/bin/python3
"""
A module to Initialize the Package
It creates an object from FileStorage Class to be
the Storage for the Project
"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
