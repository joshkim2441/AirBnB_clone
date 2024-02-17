#!/usr/bin/python3
"""Define the class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representation of a Review"""
    place_id = ""
    user_id = ""
    text = ""
