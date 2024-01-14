#!/usr/bin/python3
"""Script."""


from models.engine import file_storage


storage = file_storage.FileStorage()

storage.reload()
