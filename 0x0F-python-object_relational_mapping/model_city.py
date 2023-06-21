#!/usr/bin/python3
"""model_city
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import State

Base = declarative_base()


class City(Base):
    """City
    """
    __tablename__ = "cities"
    id = Column(primary_key=True, autoincrement=True, nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
