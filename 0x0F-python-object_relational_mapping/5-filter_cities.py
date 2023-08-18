#!/usr/bin/python3
""" script that takes in the name of a state as an argument and
 lists all cities of that state, using the database
  hbtn_0e_4_usa"""
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
    cur.execute("SELECT cities.name\
        FROM cities\
        JOIN states\
        ON cities.state_id=states.id\
        WHERE BINARY states.name = %s\
        ORDER BY cities.id ASC;", (state_name, ))
    rows = cur.fetchall()
    cities_list = []
    for i in rows:
        cities_list.append(i[0])
    print(", ".join(cities_list))
