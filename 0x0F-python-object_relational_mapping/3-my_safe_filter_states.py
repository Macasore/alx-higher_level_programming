#!/usr/bin/python3
"""3-my_safe_filter-states
sql injection script
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
    input = sys.argv[4]
    query = "SELECT * from states WHERE name LIKE binary %s\
        ORDER BY states.id ASC"
    cur.execute(query, (input,))
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
