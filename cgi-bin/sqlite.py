#!/usr/bin/env python3

import sqlite3 as lite
# import sys #&

db_file = "data.db"
con = lite.connect(db_file)

def createDB(con):
    with con:
        cur = con.cursor()
        # 1 table
        
        cur.execute("CREATE TABLE IF NOT EXISTS region (id integer PRIMARY KEY,name text NOT NULL)")
        cur.execute("INSERT INTO region VALUES (1,'Краснодарский край')")
        cur.execute("INSERT INTO region VALUES (2,'Ростовская область')")
        cur.execute("INSERT INTO region VALUES (3,'Ставропольский край')")
        # 2 table
        
        cur.execute("CREATE TABLE IF NOT EXISTS city (region_id integer NOT NULL,name text NOT NULL,FOREIGN KEY (region_id) REFERENCES region (id))")
        cur.execute("INSERT INTO city VALUES (1,'Краснодар')")
        cur.execute("INSERT INTO city VALUES (1,'Кропоткин')")
        cur.execute("INSERT INTO city VALUES (1,'Славянск')")
        cur.execute("INSERT INTO city VALUES (2,'Ростов')")
        cur.execute("INSERT INTO city VALUES (2,'Шахты')")
        cur.execute("INSERT INTO city VALUES (2,'Батайск')")
        cur.execute("INSERT INTO city VALUES (3,'Ставрополь')")
        cur.execute("INSERT INTO city VALUES (3,'Пятигорск')")
        cur.execute("INSERT INTO city VALUES (3,'Кисловодск')")

        # 3 table
        cur.execute("CREATE TABLE comments (id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,region_id	INTEGER,city_id	INTEGER,name	TEXT NOT NULL,comment	TEXT NOT NULL)")
        # sql = "INSERT INTO comments VALUES ('1','1','2','name','comment')"
        # cur.execute(sql)


    if con:
        con.close()


#если не существует db создам таблицы
# try:
#     file = open(db_file)
# except IOError as e:
#     print(u'create you base....')
#     createDB(con)
# else:
#     with file:
#         print(u'exist db')
#### нужна проверка на существования базы !!!
createDB(con)