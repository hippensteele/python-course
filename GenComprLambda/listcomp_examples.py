#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 28, 2018 10:04:35 AM$"

text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]

print(capitals)

words = [word.upper() for word in text.split(' ')]

print(words)