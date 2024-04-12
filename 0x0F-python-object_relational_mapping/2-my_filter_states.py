#!/usr/bin/python3

"""  lists all states from the database hbtn_0e_0_usa with filter """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", user=argv[1],
                                 password=argv[2], db=argv[3], port=3306)
    cursor = connection.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(argv[4]))
    data = cursor.fetchall()

    for row in data:
        print(row)
    cursor.close()
    connection.close()
