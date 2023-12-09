#!/usr/bin/python3
"""init file package"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
