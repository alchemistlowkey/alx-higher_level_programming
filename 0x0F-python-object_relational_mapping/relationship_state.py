#!/usr/bin/python3
"""
State class
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

db_metadata = MetaData()
Base = declarative_base(metadata=db_metadata)


class State(Base):
    """
    A child class of the Base class
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", backref="state", cascade="all, delete-orphan")

    def __init__(self, name):
        """
        Initializing the name
        """
        self.name = name
