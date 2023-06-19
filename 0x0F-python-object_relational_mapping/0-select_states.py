#!/usr/bin/python3
"""0-select_states module
this module creates a script that lists all the states from the database
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

    cur.execute("SELECT id, name FROM states ")
    rows = cur.fetchall()

    for row in rows:
        print(row)
