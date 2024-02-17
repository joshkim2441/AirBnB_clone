#!/usr/bin/python3
"""Initialize the global varaibles module"""

from .engine.file_storage import FileStorage
"""Storage instance retrieval"""
storage = FileStorage()
storage.reload()
