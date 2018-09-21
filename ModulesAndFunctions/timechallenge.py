#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 8, 2018 7:25:23 AM$"

import datetime
import pytz
import random

zones = list(pytz.all_timezones)
options = []

while len(options) < 9:
    n = random.randint(1, len(zones))
    if zones[n] not in options:
        options.append(zones[n])

print("Please choose a timezone from the following:")
for i in range(len(options)):
    print(i+1, options[i], sep=': ')

while True:
    try:
        choice = int(input("Choice: "))
    except ValueError:
        print("Please type a number.")
        continue
    if choice == 0:
        break
    elif choice not in range(1,len(options)+1):
        print("Not found, please try again.")
    else:
        tz_info = pytz.timezone(options[choice-1])
        dt = datetime.datetime.now(tz=tz_info)
        print("The time in {} is {}".format(options[choice-1],dt.strftime('%A %B %d %Y, %I:%M:%S %p')))
        dt = datetime.datetime.now()
        print("The local time is {}".format(dt.strftime('%A %B %d %Y, %I:%M:%S %p')))
        dt = datetime.datetime.utcnow()
        print("The current UTC time is {}".format(dt.strftime('%A %B %d %Y, %I:%M:%S %p')))


