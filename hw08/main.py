import sqlite3
from create_db import name_database


if __name__ == "__main__":
    with open('query.sql') as f:
        sql = f.read()

    with sqlite3.connect(name_database) as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        print(cursor.fetchall())
