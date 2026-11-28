#!/usr/bin/python3
"""List states matching a name provided by the user."""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    state_name = db.escape_string(sys.argv[4]).decode("utf-8")
    query = "SELECT * FROM states WHERE BINARY name = BINARY '{}' ORDER BY id ASC"
    cur.execute(query.format(state_name))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
