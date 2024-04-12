#!/usr/bin/python3
"""lists all states from the database """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", user=argv[1],
                                 password=argv[2], db=argv[3], port=3306)
    cursor = connection.cursor()
    valid = argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (valid, ))
    data = cursor.fetchall()

    for row in data:
        print(row)
    cursor.close()
    connection.close()
