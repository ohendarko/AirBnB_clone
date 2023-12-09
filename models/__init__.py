#!/usr/bin/python3
"""init file package"""
# change
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
