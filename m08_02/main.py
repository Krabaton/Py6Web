from random import randint

import psycopg2
from contextlib import contextmanager
from sqlite3 import Error
from faker import Faker
fake = Faker()


@contextmanager
def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = psycopg2.connect(host='localhost', database='test', user='postgres', password='567234')
        print(conn)
        yield conn
        conn.commit()
    except Error as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


if __name__ == '__main__':
    # sql_create_users_table = """CREATE TABLE IF NOT EXISTS users (
    #  id SERIAL PRIMARY KEY,
    #  name VARCHAR(120),
    #  email VARCHAR(120),
    #  password VARCHAR(120),
    #  age numeric CHECK (age > 10 AND age < 90)
    # );"""
    #
    # with create_connection() as conn:
    #     if conn is not None:
    #         create_table(conn, sql_create_users_table)
    #     else:
    #         print('Error: can\'t create the database connection')

    # sql_insert_users_table = "INSERT INTO users(name,email,password, age) VALUES(%s, %s, %s, %s)"
    #
    # with create_connection() as conn:
    #     if conn is not None:
    #         cur = conn.cursor()
    #         for _ in range(50000):
    #             cur.execute(sql_insert_users_table, (fake.name(), fake.email(), fake.password(), randint(11, 89)))
    #         cur.close()
    #     else:
    #         print('Error: can\'t create the database connection')

    sql_select_users_table = "SELECT * FROM users WHERE id = %s"

    with create_connection() as conn:
        if conn is not None:
            cur = conn.cursor()
            cur.execute(sql_select_users_table, (4, ))
            # print(cur.fetchall())
            print(cur.fetchone())
            cur.close()
        else:
            print('Error: can\'t create the database connection')