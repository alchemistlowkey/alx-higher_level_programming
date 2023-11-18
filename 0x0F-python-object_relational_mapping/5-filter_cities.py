#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    mydb = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    mydbcursor = mydb.cursor()
    mydbcursor.execute("SELECT cities.id, cities.name, states.name "
                       "FROM cities "
                       "JOIN states ON cities.state_id = states.id "
                       "WHERE states.name = %s "
                       "ORDER BY cities.id ASC",
                       (sys.argv[4],)
                       )
    cities = mydbcursor.fetchall()
    print(", ".join([row[1] for row in cities]))
    mydbcursor.close()
    mydb.close()
