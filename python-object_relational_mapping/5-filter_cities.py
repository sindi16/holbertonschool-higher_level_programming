#!/usr/bin/python3
"""
List all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main_":
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1], passwd=arv[2], db=argv[3])
    cursor = conn.cursor()

    cmd = "SELECT cities.name FROM cities\
        JOIN states ON states_id = cities.states_id\
        WHERE states.name LIKE BINARY %s\
        ORDER BY cities.id ASC"
    cursor.execute(cmd, (argv[4], ))
    rows = cursor.fetchall()

    result = []
    for row in rows:
        result.append(row[0])
        print(", ".join(result))
    cursor.close()
    connection.close()
