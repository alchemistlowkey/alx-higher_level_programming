#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa
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
    mydbcursor.execute("SELECT * FROM states "
                       "WHERE name LIKE BINARY '{}' "
                       "ORDER BY states.id ASC;".format(sys.argv[4]))
    states = mydbcursor.fetchall()
    for data in states:
        print(data)
    mydbcursor.close()
    mydb.close()
