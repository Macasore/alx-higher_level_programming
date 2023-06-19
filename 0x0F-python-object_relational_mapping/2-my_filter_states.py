#!/usr/bin/python3
"""2-my_filter_states
a script that takes in an argument and displays all values in the states
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
    state_name = sys.argv[4]
    db = MySQLdb.connect(**connections)
    cur = db.cursor()
    query = ("SELECT * from states WHERE name like '{}' ORDER BY states.id ASC"
             .format(sys.argv[4]))
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
