#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class User(BaseModel, Base):
    """This class defines a user by various attributes
    Attributes:
        __tablename__ (str): represents the table name, users
        email (str): represents a column containing a string
        password (str): represents a column containing a string
        first_name (str): represents a column containing a string
        last_name (str): represents a column containing a string
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
