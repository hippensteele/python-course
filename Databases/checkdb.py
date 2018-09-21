#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 22, 2018 2:34:57 PM$"

import sqlite3

db = sqlite3.connect("contacts.sqlite")

name = input("Type in a name to find: ") # Tim

#name = name, # convert string to tuple (note comma)
#for item in db.execute("select * from contacts where name = ?", name):
#    print(item)

for item in db.execute("select * from contacts where name = ?", (name,)): # parentheses and comma convert to tuple
    print(item)


db.close()