#!/usr/bin/python3
"""
List all states from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cursor = conn.cursor()
    query = "SELECT * FROM states\
            WHERE name LIKE %s\
            ORDER BY states.id"
    cursor.execute(query, (argv[4], ))
    all_rows = cursor.fetchall()

    for row in all_rows:
        print(row)

    cursor.close()
    conn.close()
