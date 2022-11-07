#!/usr/bin/python3
"""Class named Review that Inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""

    place_id = ""
    user_id = ""
    text = ""
