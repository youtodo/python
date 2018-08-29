#!/usr/bin/env python3
db_file = "data.db"

import sqlite3 as lite
# import sys
import cgi

form = cgi.FieldStorage()
allcomments = form.getfirst("allcomments", "all")

con = lite.connect(db_file)
cursor = con.cursor()

print("Content-type: text/plain\n")

sql = "SELECT com.id,r.name,c.name,com.name,com.comment FROM comments com left join region r on r.id=com.region_id left join city c on c.id=com.city_id"
cursor.execute(sql)

print (cursor.fetchall())