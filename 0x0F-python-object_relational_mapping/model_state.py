#!/usr/bin/python3

"""state class and base instance of decarative base ()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

myMeta = MetaData()
Base = declarative_base(metadata=myMeta)


class State(Base):
    """
    Class State with id , name
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
