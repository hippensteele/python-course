#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 28, 2018 7:35:33 AM$"

def odds_gen():
    start = 1
    while True:
        yield start
        start += 2

odds = odds_gen()
for i in range(100):
    print(next(odds))