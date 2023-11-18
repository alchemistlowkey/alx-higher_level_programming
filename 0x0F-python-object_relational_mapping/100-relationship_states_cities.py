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
    Base.metadata.create_all(mydb_engine)
    Session = sessionmaker(bind=mydb_engine)
    session = Session()

    california = State(name="California")
    san_francisco = City(name="San Francisco")
    california.cities.append(san_francisco)

    session.add(california)
    session.add(san_francisco)
    session.commit()
    session.close()
