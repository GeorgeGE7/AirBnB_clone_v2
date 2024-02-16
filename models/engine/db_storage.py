#!/usr/bin/python3
"""_summary_
"""
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.exc import InvalidRequestError
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class DBStorage():
    """_summary_
    """
    __engine = None
    __session = None
    def __init__(self):
        un = getenv("HBNB_MYSQL_USER")
        pswd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        dbn = getenv("HBNB_MYSQL_DB")
        dburl = f"mysql+mysqldb://{un}:{pswd}@{host}/{dbn}"
        self.__engine = create_engine(dburl, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """_summary_

        Args:
            cls (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        objects = []
        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except Exception:
                    pass
            if issubclass(cls, Base):
                objects = self.__session.query(cls).all()
        else:
            for childcls in Base.__subclasses__():
                objects.extend(self.__session.query(childcls).all())
        instance_dict = {}
        for obj in objects:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            instance_dict[key] = obj
        return instance_dict

    def new(self, obj):
        """_summary_

        Args:
            obj (object): new object
        """
        if self and obj:
          self.__session.add(obj)
          self.__session.commit()

    def save(self):
        """_summary_
        """
        if self:
          self.__session.commit()    

    def delete(self, obj=None):
        """_summary_

        Args:
            obj (_type_, optional): _description_. Defaults to None.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """_summary_
        """
        Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        fact_ss = sessionmaker(bind=self.__engine, expire_on_commit=False)
        ss = scoped_session(fact_ss)
        self.__session = ss()