#!/usr/bin/python3
""" module for model city """

from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base


class City(Base):
    """ table city instance """
    __tablename__ = "cities"

    id = Column(Integer,  autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
