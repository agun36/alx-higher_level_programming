#!/usr/bin/python3
""" script that filters safely"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    state_name = argv[4]
    cur = db.cursor()
    """The execute function requires one parameter, the query."""
    cur.execute("SELECT * FROM states\
         WHERE BINARY name=%s\
            ORDER BY id ASC", (state_name,))
    """Obtaining Query Results"""
    rows = cur.fetchall()
    for i in rows:
        print(i)
