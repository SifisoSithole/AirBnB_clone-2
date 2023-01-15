#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


if getenv("HBNB_TYPE_STORAGE") == "db":
    class Amenity(BaseModel, Base):
        """Representation of Amenity """
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
else:
    class Amenity(BaseModel):
        """Representation of Amenity """
        name = ""

