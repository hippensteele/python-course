#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 25, 2018 5:13:08 AM$"

def average(*args): # the star packs the list of arguments sent into a tuple
    print(type(args))
    print("args is {}:".format(args))
    print("*args is:", *args)
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)

print(average(1, 2, 3, 4))

print('*' * 40)

def build_tuple(*args):
#    list = []
#    for arg in args:
#        list.append(arg)
#    return tuple(list)
    return args

number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
print(type(number_tuple))
print(number_tuple)

print('*' * 40)

list = [1, 2, 3, 4, 5]
print(list)
print(*list) # * unpacks lists as well as tuples

print('*' * 40)

#def print_backwards(*args, file=None):
#def print_backwards(*args, end=' ', **kwargs):
def print_backwards(*args, **kwargs):
#    print(kwargs)
#    keywords = {}
#    for k in kwargs.keys():
#        if k != 'end':
#            keywords[k] = kwargs[k]
    kwargs.pop('end', None)
    for word in args[::-1]:
#        print(word[::-1], end=' ', file=file)
#        print(word[::-1], end=' ', **kwargs)
#        print(word[::-1], end=' ', **keywords)
        print(word[::-1], end=' ', **kwargs)

print_backwards("hello", "world", "take", "me", "to", "your", "leader")
with open("backwards.txt", 'w') as backwards:
    print_backwards("hello", "world", "take", "me", "to", "your", "leader", file=backwards, end=' ')
print_backwards("hello", "world", "take", "me", "to", "your", "leader", sep='|') # doesn't work

print()
print('*' * 40)

def print_backwards2(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for word in args[:0:-1]: # range excludes first word
        print(word[::-1], end=sep_character, **kwargs)
    print(args[0][::-1], end=end_character, *kwargs) # print the first word separately to avoid extra sep at end

print_backwards2("hello", "world", "take", "me", "to", "your", "leader")
print_backwards2("hello", "world", "take", "me", "to", "your", "leader", sep='|')

print('*' * 40)

# the real way to do this (above were to demo args, kwargs)
def print_backwards3(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)

print_backwards3("hello", "world", "take", "me", "to", "your", "leader", sep='|')






