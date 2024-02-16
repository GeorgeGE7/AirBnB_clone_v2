#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    try:
      storage = DBStorage()
    except Exception:
       print("Can't connect to DB")
else:
    from models.engine.file_storage import FileStorage
    try:
      storage = FileStorage()
    except Exception:
        print("Can't connect to FileStorage")

try:
  storage.reload()
except Exception:
   print("Error with reload")