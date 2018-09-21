#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 22, 2018 3:07:33 PM$"

def factorial(n):
    if n <= 1:
        return 1
    else:
        print(n / 0)
        return n * factorial(n-1)

try:
    print(factorial(1000))
#except RecursionError:
#    print("This program cannot calculate factorials that large.")
#except ZeroDivisionError:
#    print("What are you doing dividing by zero???")
except (RecursionError, ZeroDivisionError):
    print("Error occurred")
