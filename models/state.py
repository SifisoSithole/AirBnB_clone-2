#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    class State(BaseModel, Base):
        """Represents a state in mysql
        attributes:
            __tablename__ (str): Name of the MySQL table
            name (str): State name
        """
        cities = relationship("City", backref="state", cascade="all, delete")
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
else:
    class State(BaseModel):
        """Represents a state in mysql"""
        @property
        def cities(self):
            """Returns a list of cities for the current state"""
            cityList = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    cityList.append(city)
            return cityList
