#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    mydb = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    mydb_engine = create_engine(mydb)
    Session = sessionmaker(bind=mydb_engine)
    session = Session()

    states = session.query(State).filter(State.name.like(
            "%a%")).order_by(State.id)
    for data in states:
        print("{}: {}".format(data.id, data.name))
