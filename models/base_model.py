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

    def __init__(self, *isadl, **all_isadl):
        """Create ot update the init
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if all_isadl:
            for t_atrr, atrr_value in all_isadl.items():
                if t_atrr == "created_at" or t_atrr == "updated_at":
                    atrr_value = datetime.strptime(atrr_value, "%Y-%m-%dT%H:%M:%S.%f")
                if hasattr(self, t_atrr):
                    setattr(self, t_atrr, atrr_value)

    def __str__(self):
        """string for an object

        Returns:
            string: string object represntation
        """
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        string_rep = f'[{cls}] ({self.id}) {self.__dict__}'
        return string_rep

    def save(self):
        """To save
        """
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """To dict function

        Returns:
            dict: dict represntation
        """
        dict_to_update_to_dict = {}
        dict_to_update_to_dict.update(self.__dict__)
        cls_val = (str(type(self)).split('.')[-1]).split('\'')[0]
        dict_to_update_to_dict.update({'__class__': cls_val})
        formated_created_at = self.created_at.isoformat()
        formated_updated_at = self.updated_at.isoformat()
        dict_to_update_to_dict['created_at'] = formated_created_at
        dict_to_update_to_dict['updated_at'] = formated_updated_at
        try:
            del dict_to_update_to_dict["_sa_instance_state"]
        except Exception:
            pass
        return dict_to_update_to_dict

    def delete(self):
        """Delete object
        """
        from models import storage
        storage.delete(self)