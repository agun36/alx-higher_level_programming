#!/usr/bin/python3
""" script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    cur = db.cursor()
    """The execute function requires one parameter, the query."""
    cur.execute("SELECT * FROM states\
        WHERE name LIKE BINARY 'N%' \
            ORDER BY id ASC")
    """Obtaining Query Results"""
    rows = cur.fetchall()
    for i in rows:
        print(i)
