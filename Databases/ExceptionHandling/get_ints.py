#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 22, 2018 3:28:43 PM$"

#try:
#    int1 = int(input("Please type in a number: "))
#    int2 = int(input("Please type in a number to divide it by: "))
#    try:
#        print(int1 / int2)
#    except ZeroDivisionError:
#        print("Can't divide by zero.")
#except ValueError:
#    print("Integer required")

import sys

def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered; please try again.")
        except EOFError: # Ctl-D
            print("Exiting program")
            sys.exit(1)
        finally:
            print("The finally clause always executes")

first_number = getint("Please type in a number: ")
second_number = getint("Please type in a number to divide it by: ")

try:
    print("{} divided by {} is {}.".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("Cannot divide by zero.")
    sys.exit(2)
else: # finally always executes; else only executes if the try completes
    print("Division successful; the else clause executes only if no exceptions were raised.")
