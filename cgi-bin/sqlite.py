#!/usr/bin/env python3

import sqlite3
from sqlite3 import Error
 
db_file = "data.db"
sql_create_region_table = """ CREATE TABLE IF NOT EXISTS region (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL
                                );"""
 
sql_create_city_table = """CREATE TABLE IF NOT EXISTS city (
                                id integer PRIMARY KEY,
                                region_id integer NOT NULL,
                                name text NOT NULL,                                
                                FOREIGN KEY (region_id) REFERENCES region (id)
                            );"""
def exec_sql(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_connection(db):
    """ create a database connection to a SQLite database """
    try:
        print("Content-type: text/html\n")
        print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>db</title>
        </head>
        <body> <h2>sqlite3.version""")
        print(sqlite3.version)

        conn = sqlite3.connect(db)
        exec_sql(conn, sql_create_region_table) 
        # exec_sql(conn, "INSERT INTO region (name) VALUES ('Краснодарский');")
        
        exec_sql(conn, sql_create_city_table)        

    except Error as e:
        print(e)
    finally:
        print(".</h2></body>")
        conn.close()

create_connection(db_file)