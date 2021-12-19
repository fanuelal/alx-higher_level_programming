#!/usr/bin/python3
"""model city"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
 
Base = declarative_base()


class City(Base):
    """ city module"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False, unique=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
