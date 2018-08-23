#!/usr/bin/env python3
# Импортируем библиотеку, соответствующую типу нашей базы данных 
import sqlite3
from sqlite3 import Error
 
db_file = "data.db"
sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    begin_date text,
                                    end_date text
                                ); """
 
sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                priority integer,
                                status_id integer NOT NULL,
                                project_id integer NOT NULL,
                                begin_date text NOT NULL,
                                end_date text NOT NULL,
                                FOREIGN KEY (project_id) REFERENCES projects (id)
                            );"""
def create_table(conn, create_table_sql):
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
        create_table(conn, sql_create_projects_table)
        create_table(conn, sql_create_tasks_table)        

    except Error as e:
        print(e)
    finally:
        print(".</h2></body>")
        conn.close()

create_connection(db_file)