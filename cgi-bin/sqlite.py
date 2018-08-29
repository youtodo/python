#!/usr/bin/env python3

import sqlite3 as lite
# import sys #&

db_file = "data.db"
con = lite.connect(db_file)

def createDB(con):
    with con:
        cur = con.cursor()
        # 1 table
        
        cur.execute("CREATE TABLE IF NOT EXISTS region (id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,name text NOT NULL)")
        cur.execute("INSERT INTO region (name) VALUES ('Краснодарский край')")
        cur.execute("INSERT INTO region (name) VALUES ('Ростовская область')")
        cur.execute("INSERT INTO region (name) VALUES ('Ставропольский край')")
        # 2 table
        
        cur.execute("CREATE TABLE IF NOT EXISTS city  (id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,region_id integer NOT NULL,name text NOT NULL,FOREIGN KEY (region_id) REFERENCES region (id))")
        cur.execute("INSERT INTO city (region_id,name) VALUES (1,'Краснодар')")
        cur.execute("INSERT INTO city (region_id,name) VALUES (1,'Кропоткин')")
        cur.execute("INSERT INTO city (region_id,name) VALUES (1,'Славянск')")
        cur.execute("INSERT INTO city (region_id,name) VALUES (2,'Ростов')")
        cur.execute("INSERT INTO city (region_id,name) VALUES (2,'Шахты')")
        cur.execute("INSERT INTO city (region_id,name) VALUES (2,'Батайск')")
        cur.execute("INSERT INTO city (region_id,name) VALUES (3,'Ставрополь')")
        cur.execute("INSERT INTO city (region_id,name) VALUES (3,'Пятигорск')")
        cur.execute("INSERT INTO city (region_id,name) VALUES (3,'Кисловодск')")

        # 3 table
        cur.execute("CREATE TABLE comments (id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,region_id	INTEGER,city_id	INTEGER,name	TEXT NOT NULL,comment	TEXT NOT NULL)")
        cur.execute("INSERT INTO comments (region_id,city_id,name,comment) VALUES (1,1,'Иванов 1','Тестовый комментарий №1')")
        cur.execute("INSERT INTO comments (region_id,city_id,name,comment) VALUES (2,4,'Иванов 2','Тестовый комментарий №2')")
        cur.execute("INSERT INTO comments (region_id,city_id,name,comment) VALUES (2,4,'Иванов 3','Тестовый комментарий №3')")
        cur.execute("INSERT INTO comments (region_id,city_id,name,comment) VALUES (1,3,'Иванов 4','Тестовый комментарий №4')")
        cur.execute("INSERT INTO comments (region_id,city_id,name,comment) VALUES (1,3,'Иванов 4','Тестовый комментарий №4')")
        cur.execute("INSERT INTO comments (region_id,city_id,name,comment) VALUES (1,3,'Иванов 4','Тестовый комментарий №4')")
        cur.execute("INSERT INTO comments (region_id,city_id,name,comment) VALUES (1,3,'Иванов 4','Тестовый комментарий №4')")
        cur.execute("INSERT INTO comments (region_id,city_id,name,comment) VALUES (1,3,'Иванов 4','Тестовый комментарий №4')")
        cur.execute("INSERT INTO comments (region_id,city_id,name,comment) VALUES (1,3,'Иванов 4','Тестовый комментарий №4')")
        cur.execute("INSERT INTO comments (region_id,city_id,name,comment) VALUES (2,5,'Иванов 5','Тестовый комментарий №5')")
        cur.execute("INSERT INTO comments (region_id,city_id,name,comment) VALUES (3,7,'Иванов 6','Тестовый комментарий №6')")
        cur.execute("INSERT INTO comments (region_id,city_id,name,comment) VALUES (1,3,'Иванов 4','Тестовый комментарий №4')")
        cur.execute("INSERT INTO comments (region_id,city_id,name,comment) VALUES (1,3,'Иванов 4','Тестовый комментарий №4')")
        cur.execute("INSERT INTO comments (region_id,city_id,name,comment) VALUES (1,3,'Иванов 4','Тестовый комментарий №4')")
        cur.execute("INSERT INTO comments (region_id,city_id,name,comment) VALUES (1,1,'Иванов 11','Тестовый комментарий №11')")
        cur.execute("INSERT INTO comments (region_id,city_id,name,comment) VALUES (2,5,'Иванов 22','Тестовый комментарий №22')")
        cur.execute("INSERT INTO comments (region_id,city_id,name,comment) VALUES (2,4,'Иванов 33','Тестовый комментарий №33')")
        cur.execute("INSERT INTO comments (region_id,city_id,name,comment) VALUES (1,3,'Иванов 44','Тестовый комментарий №44')")
        cur.execute("INSERT INTO comments (region_id,city_id,name,comment) VALUES (2,5,'Иванов 55','Тестовый комментарий №55')")
        cur.execute("INSERT INTO comments (region_id,city_id,name,comment) VALUES (3,8,'Иванов 66','Тестовый комментарий №66')")
        
        # sql = "INSERT INTO comments VALUES ('1','1','2','name','comment')"
        # cur.execute(sql)


    if con:
        con.close()
createDB(con)