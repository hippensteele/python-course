#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 10, 2018 5:42:45 AM$"

#def center_text(text):
#    text = str(text)
#    margin = (80 - len(text)) // 2
#    print(margin * " " + text)

def center_text(*args, sep=' ', end='\n', file=None, flush=False): # '*' signals multiple args
    text = ""
    for arg in args:
        text += str(arg) + sep # list comprehension would be more efficient, and allow skipping final sep
    margin = (80 - len(text)) // 2
    print(margin * " " + text, end=end, file=file, flush=flush)

center_text("spam and eggs")
center_text("spam, spam, spam")
center_text(12)
center_text("spam", "spam", "spam", "spam", "spam", sep=":")

def center_text2(*args, sep=' '): # '*' signals multiple args
    text = ""
    for arg in args:
        text += str(arg) + sep # list comprehension would be more efficient, and allow skipping final sep
    margin = (80 - len(text)) // 2
    return margin * " " + text

print(center_text2("spam and eggs"))
print(center_text2("spam, spam, spam"))
print(center_text2(12))
print(center_text2("spam", "spam", "spam", "spam", "spam", sep=":"))
