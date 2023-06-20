#!/usr/bin/python3
"""4-cities_by_state
Write a script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    connections = {
        "user": sys.argv[1],
        "passwd": sys.argv[2],
        "db": sys.argv[3],
        "host": "localhost",
        "port": 3306
    }
    db = MySQLdb.connect(**connections)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name from states,\
        cities WHERE cities.state_id=states.id ORDER BY cities.id ")
    rows = cur.fetchall()

    for row in rows:
        print(row)
