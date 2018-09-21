#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 28, 2018 6:41:33 AM$"

import sys

def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start
        print("my_range after yield")
        start += 1

_ = input("A")
#big_range = range(5)
big_range = my_range(5)
_ = input("B")

print(next(big_range))

print("big_range is {} bytes".format(sys.getsizeof(big_range)))

big_list = []

_ = input("C")
for val in big_range:
    _ = input("D")
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)