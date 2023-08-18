#!/usr/bin/python3
"""script that prints the first State object from the database
hbtn_0e_6_usa"""
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State).filter(State.name.contains('a'))
    for i in first_state:
        session.delete(i)
    session.commit()
    session.close()
