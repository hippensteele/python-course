#!/usr/bin/python3
# name = input("Please input your name: ")
# age = int(input("How old are you, {}? ".format(name)))

# if age >= 18:
#     print("You are old enough to vote.")
#     print("Please put an X in the box.")
# else:
#     print("Please come back in {} years.".format(18-age))

# print("Please guess a number between one and ten: ")
# guess = int(input())
# if guess < 5:
#     print("Please guess higher:")
#     guess = int(input())
#     if guess == 5:
#         print("Well done; you guessed it.")
#     else:
#         print("Sorry, you have not guessed correctly.")
# elif guess > 5:
#     print("Please guess lower:")
#     guess = int(input())
#     if guess == 5:
#         print("Well done; you guessed it.")
#     else:
#         print("Sorry, you have not guessed correctly.")
# else:
#     print("You got it, first time!")

# print("Please guess a number between 1 and 10: ")
# guess = int(input())
# if guess == 5:
#     print("You got, first time!")
# else:
#     if guess < 5:
#         print("Please guess higher.")
#     else:
#         print("Please guess lower.")
#     guess = int(input())
#     if guess == 5:
#         print("You got it.")
#     else:
#         print("Sorry.")

# age = int(input("How old are you? "))
### if age >= 16 and age <= 65:
# if 16 <= age <= 65:
#     print("Have a good day at work.")

# if age < 16 or age > 65:
#     print("Enjoy your free time.")
# else:
#     print("Have a good day at work.")

# bool = "false"
# if bool:
#     print("true")
# else:
#     print("false")
    
# bool = False 
# if bool:
#     print("true")
# else:
#     print("false")
    
# bool = 0
# if bool:
#     print("true")
# else:
#     print("false")

# print("{},{},{},{},{},{}".format(False,bool(None),bool(True),bool(0),bool(-1),bool("False")))

# print(not False)
# print(not True)

parrot = "Norwegian Blue"
letter = input("Give me a letter: ")
if letter not in parrot:
    print("I don't need that letter.")
else:
    print("Give me an '{}', Bob!".format(letter))
