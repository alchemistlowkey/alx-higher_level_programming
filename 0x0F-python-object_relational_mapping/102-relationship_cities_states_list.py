#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    mydb = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    mydb_engine = create_engine(mydb)
    Session = sessionmaker(bind=mydb_engine)
    session = Session()

    cities = session.query(City).order_by(City.id)

    for data in cities:
        state_name = data.state.name if data.state else "Not Found"
        print("{}: {} -> {}".format(data.id, data.name, state_name))

    session.close()
