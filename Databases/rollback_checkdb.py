#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 23, 2018 6:02:28 AM$"

import sqlite3, pytz

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT * FROM history"):
#    local_time = row[0]
#    print("{}\t{}".format(local_time, type(local_time)))
    utc_time = row[0]
    local_time = pytz.utc.localize(utc_time).astimezone()
    print("{}\t{}".format(utc_time, local_time))

print('*' * 40)

for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime, "
                                "history.account, history.amount FROM history ORDER BY history.time"):
    print(row)

print('*' * 40)

for row in db.execute("SELECT * FROM localhistory"):
    print(row)

db.close()