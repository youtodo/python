#!/usr/bin/env python3
db_file = "data.db"

import sqlite3 as lite
# import sys
import cgi

form = cgi.FieldStorage()
idcomment = form.getfirst("idcomment", "0")

con = lite.connect(db_file)
cursor = con.cursor()

print("Content-type: text/plain\n")
print("DELETE:",idcomment)

sql = "DELETE FROM COMMENTS WHERE id=:idcomment"
cursor.execute(sql,{"idcomment":idcomment})
con.commit()
con.close()