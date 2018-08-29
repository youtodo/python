#!/usr/bin/env python3
import cgi
import sqlite3 as lite

db_file = "data.db"
form = cgi.FieldStorage()
lastname = form.getfirst("lastName", "empty")
name = form.getfirst("name", "empty")
patronymic = form.getfirst("patronymic", "empty")
region = form.getfirst("region", "1")
city = form.getfirst("city", "1")
phone = form.getfirst("phone", "1")
mail = form.getfirst("mail", "empty")
comment = form.getfirst("comment", "empty")

con = lite.connect(db_file)
def inCommentDB(con):
    with con:
        cur = con.cursor()
        sql = "INSERT INTO comments(region_id,city_id,name,comment) VALUES (:region,:city,:name,:comment)"
        cur.execute(sql,{"region":region,"city":city,"name":name, "comment": comment })

inCommentDB(con)
con.close() 
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")
print("<p><a class='button' href='/'>на главную</a></p>")
print("<h2>Обработка данных форм!</h2>")
print("<p>lastName: {}</p>".format(lastname))
print("<p>name: {}</p>".format(name))
print("<p>patronymic: {}</p>".format(patronymic))
print("<p>region: {}</p>".format(region))
print("<p>city: {}</p>".format(city))
print("<p>phone: {}</p>".format(phone))
print("<p>mail: {}</p>".format(mail))
print("<p>comment: {}</p>".format(comment))


print("""</body>
        </html>""")