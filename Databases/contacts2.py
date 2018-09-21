#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 22, 2018 6:58:35 AM$"

import sqlite3

new_email = "newemail@email.com"
phone = input("Please input a phone number: ") # 1234

db = sqlite3.connect("contacts.sqlite")

update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"
update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))
print("{} rows updated".format(update_cursor.rowcount))
update_cursor.connection.commit()
update_cursor.close()

for row in db.execute("SELECT * FROM contacts"):
    print(row)

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name, phone, email)

db.close()