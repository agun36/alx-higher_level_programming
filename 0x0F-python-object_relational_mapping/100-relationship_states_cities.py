#!/usr/bin/python3
"""script that prints the first State object from the database
hbtn_0e_6_usa"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    session.add(new_state)

    session.commit()
    session.close()
