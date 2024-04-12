#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", user=argv[1],
                                 passwd=argv[2], db=argv[3], port=3306)
    cursor = connection.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    connection.close()
