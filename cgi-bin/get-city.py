#!/usr/bin/env python3
db_file = "data.db"

import sqlite3 as lite
# import sys
import cgi

form = cgi.FieldStorage()
idcity = form.getfirst("idcity", "1")

con = lite.connect(db_file)
cursor = con.cursor()

print("Content-type: text/plain\n")

sql = "SELECT c.name, (SELECT count(*) from comments com WHERE com.city_id=c.id) as count FROM city c where c.id=:idcity"
cursor.execute(sql,{"idcity": idcity})

print (cursor.fetchall())