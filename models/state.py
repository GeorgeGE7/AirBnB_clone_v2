#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel):
    """inherits from BaseModel and Base

    Args:
        BaseModel (BaseModel): the base model
        Base (declarative_base): from sqlalchemy
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete-orphan')
