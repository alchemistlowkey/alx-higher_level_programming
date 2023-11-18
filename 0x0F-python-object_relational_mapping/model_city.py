#!/usr/bin/python3
"""
City class
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """
    A child class of the Base class
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
