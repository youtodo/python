#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
lastname = form.getfirst("lastName", "не задано")
name = form.getfirst("name", "не задано")
patronymic = form.getfirst("patronymic", "не задано")
region = form.getfirst("region", "не задано")
city = form.getfirst("city", "не задано")
phone = form.getfirst("phone", "не задано")
mail = form.getfirst("mail", "не задано")
comment = form.getfirst("comment", "не задано")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

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