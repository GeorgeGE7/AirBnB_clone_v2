#!/usr/bin/python3
"""_summary_
Returns:
    _type_: _description_
"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String

Base = declarative_base()


class BaseModel:
    """_summary_

    Returns:
        _type_: _description_
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new base model that will be inherted"""
        self.id = str(uuid.uuid4())
        if not kwargs:
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        if kwargs:
            date_formate = "%Y-%m-%dT%H:%M:%S.%f"
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, date_formate)
                if hasattr(self, k):
                    setattr(self, k, v)

    def __str__(self):
        """Function to make the obj string

        Returns:
            String: Object as a string
        """
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return f'[{cls}] ({self.id}) {self.__dict__}'

    def save(self):
        """To save the new objs
        """
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        new_dict = {}
        new_dict.update(self.__dict__)
        new_dict.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        try:
            del new_dict["_sa_instance_state"]
        except Exception:
            pass
        return new_dict

    def delete(self):
        """Function that delete an obj
        """
        from models import storage
        storage.delete(self)