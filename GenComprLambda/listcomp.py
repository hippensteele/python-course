#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 28, 2018 9:50:55 AM$"

numbers = [1, 2, 3, 4, 5]
squares = []
for number in numbers:
    squares.append(number ** 2)
print(squares)

squares = [number ** 2 for number in numbers]
print(squares)