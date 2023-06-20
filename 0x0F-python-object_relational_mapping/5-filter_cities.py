#!/usr/bin/python3
"""5-filter_cities
a script that takes in the name of a state as an argument
and lists all cities of that state, using the database
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
    state_name = sys.argv[4]
    query = "SELECT name from cities WHERE cities.state_id\
        =(SELECT id from states where name=%s) ORDER BY cities.id"
    cur.execute(query, (state_name, ))
    rows = cur.fetchall()
    value = []
    for row in rows:
        for col in row:
            value.append(col)
    print(', '.join(value))
