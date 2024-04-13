#!/usr/bin/python3

from SQLAlchemy import Column, Integer, String, MetaData
from SQLAlchemy.ext.declarative import declarative_base

myMeta = MetaData()

Base = decarative_base(metadata=myMeta)


class State(Base):
    """
    Class State with id , name 
    """

    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
