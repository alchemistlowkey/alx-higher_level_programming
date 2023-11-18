#!/usr/bin/python3
"""
A script that lists all City objects from the database hbtn_0e_6_usa
"""

from sys import argv
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    mydb = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    mydb_engine = create_engine(mydb)
    Session = sessionmaker(bind=mydb_engine)
    session = Session()

    cities = session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id)

    for key, value in cities:
        print("{}: ({}) {}".format(value.name, key.id, key.name))
