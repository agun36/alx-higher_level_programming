#!/usr/bin/python3
"""script that lists all State objects, and corresponding City
 objects, contained in the database hbtn_0e_101_usa"""
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id)
    for states in result:
        print("{}: {}".format(st.id, st.name))
        for city in states.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
