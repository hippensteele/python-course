#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 7, 2018 7:02:12 PM$"

import pytz
import datetime

country = 'Europe/Moscow'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time is {} in {}.".format(local_time, country))
print("UTC is {}.".format(datetime.datetime.utcnow()))

#for x in pytz.all_timezones:
#    print(x)
#print()

### netbeans stdout is US-ASCII; bombs on other characters
import sys
if sys.stdout.encoding == 'US-ASCII':
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

#for x in sorted(pytz.country_names):
#    print(x + ": " + pytz.country_names[x])

#for x in sorted(pytz.country_names):
#    print("{}: {}:  {}".format(x, pytz.country_names[x], pytz.country_timezones.get(x)))

for x in sorted(pytz.country_names):
#    print("{}: {}".format(x, pytz.country_names[x]), end=': ')
    print("{}: {}".format(x, pytz.country_names[x]))
    if x in pytz.country_timezones:
#        print(pytz.country_timezones[x])
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tTime zone not defined.")



    