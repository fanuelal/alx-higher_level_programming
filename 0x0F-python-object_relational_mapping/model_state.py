#!/usr/bin/python3
""" a python file that contains the class definition of a State"""
from SQLAlchemy import Column, Integer, String
from SQLAlchemy.ext.declarative import declarative_base
Base = declarative_base()
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key = True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    
