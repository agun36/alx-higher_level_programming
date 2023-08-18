#!/usr/bin/python3
"""lists all City objects from the database hbtn_0e_101_usa"""
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """Connecting database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State)
    for states in result:
        for city in states.cities:
            print("{}: {} -> {}".format(city.id, city.name, states.name))
    session.close()
