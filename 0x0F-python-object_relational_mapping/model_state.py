#!/usr/bin/python3
"""model_state
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):
    """State
    This is the state class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
