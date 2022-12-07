#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey



class Place(BaseModel, Base):
    """ A place to stay 
    Attributes:
        __tablename__ (str): represents the table name, places
        user_id (str): represents a column containing a string
        name (str): represents a column containing a string
        description (str): represents a column containing a string
        number_rooms (int): represents a column containing an integer
        number_bathrooms (int): represents a column containing an integer
        max_guest (int): represents a column containing an integer
        price_by_night (int): represents a column containing an integer
        latitude (float): represents a column containing a float
        longitude (float): represents a column containing a float
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
