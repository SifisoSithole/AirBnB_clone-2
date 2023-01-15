#!/usr/bin/python3
"""
This is the database object

It handles the database storage
"""
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class DBStorage:
    """ Handles database storage
    attributes:
        __engine: Private class attribute for the engine object
        __session: Private class attribute for the session object
    """
    __engine = None
    __session = None

    def __init__(self):
        conn_str = f'mysql+mysqldb://{environ["HBNB_MYSQL_USER"]}:{environ["HBNB_MYSQL_PWD"]}@{environ["HBNB_MYSQL_HOST"]}/{environ["HBNB_MYSQL_DB"]}'
        self.__engine = create_engine(conn_str, pool_pre_ping=True)
        if "HBNB_ENV" in environ.keys():
            if environ["HBNB_ENV"] == 'test':
                Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns all objects depending of the class name
        arguments:
            cls (class): Class to query or all classes if cls is None
        Return: Returns a dictionary
        """
        obj_dict = {}
        objs = []
        if cls is not None:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f'{type(obj).__name__}.{obj.id}'
                obj_dict[key] = obj
        else:
            objs.append(self.__session.query(User).all())
            objs.append(self.__session.query(State).all())
            objs.append(self.__session.query(City).all())
            objs.append(self.__session.query(Place).all())
            #objs.append(self.__session.query(Amenity).all())
            #objs.append(self.__session.query(Review).all())
            for lst in objs:
                for obj in lst:
                    key = f'{type(obj).__name__}.{obj.id}'
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """closes a session"""
        self.__session.close()
