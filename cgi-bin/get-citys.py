#!/usr/bin/env python3
db_file = "data.db"

import sqlite3 as lite
# import sys
import cgi

form = cgi.FieldStorage()
idregion = form.getfirst("idregion", "1")

con = lite.connect(db_file)
cursor = con.cursor()

print("Content-type: text/plain\n")

sql = "SELECT c.name FROM city c WHERE c.region_id=:idreg"
cursor.execute(sql,{"idreg": idregion})

print (cursor.fetchall())