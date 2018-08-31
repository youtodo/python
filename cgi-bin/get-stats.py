#!/usr/bin/env python3
db_file = "data.db"

import sqlite3 as lite
# import sys
import cgi

form = cgi.FieldStorage()
stats = form.getfirst("stats", "all")

con = lite.connect(db_file)
cursor = con.cursor()

print("Content-type: text/plain\n")

# sql = "SELECT com.id FROM comments com where com.region_id=2"
sql = "SELECT r.name, (SELECT count(*) from comments com WHERE com.region_id=r.id) as count, r.id FROM region r"
sql = "SELECT r.name, (SELECT count(*) from comments com WHERE com.region_id=r.id) as count FROM region r"

cursor.execute(sql)

print (cursor.fetchall())