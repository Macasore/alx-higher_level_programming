#!/usr/bin/python3
"""1-filter_states
this script lists all states with a name starting with N from the database
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
    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ")
    rows = cur.fetchall()

    for row in rows:
        print(row)
