#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLconnection
from sys import argv


if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], connection=argv[3], port=3306)
    cursor = connection.cursor()
    cursor.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (argv[4],))
    rows = cursor.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cursor.close()
    connection.close()
