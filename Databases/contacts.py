#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 22, 2018 6:38:22 AM$"

import sqlite3

db = sqlite3.connect("contacts.sqlite")

#db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
#db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 6545678, 'tim@email.com')")
#db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@myemail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

#print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

#for row in cursor:
#    print(row)
for name, phone, email in cursor:
    print(name, phone, email)
cursor.close()

db.commit()
db.close()
