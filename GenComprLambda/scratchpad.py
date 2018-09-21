#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 28, 2018 7:18:42 AM$"

a = 2
b = 3
print("a is {}, b is {}".format(a,b))

a, b = b, a
print("a is {}, b is {}".format(a,b))
