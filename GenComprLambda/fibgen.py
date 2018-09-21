#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 28, 2018 7:23:36 AM$"

def fibonacci():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current

fib = fibonacci()
for i in range(21):
    print(next(fib))
