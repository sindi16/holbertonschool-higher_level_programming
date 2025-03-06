#!/usr/bin/python3
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )

    cursor = db.cursor()
    cursor.execute('SELECT * FROM states\
                    WHERE name LIKE "N%"\
                    ORDER BY states.id')
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()