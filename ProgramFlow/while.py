# for i in range(10):
#     print("i is now {}".format(i))
    
# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1 
    
# available_exits = ["south","east","west"]
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose an exit: ")
#     if chosen_exit == "quit":
#         print("Game over.")
#         break
# else: # doesn't execute after break
#     print("Aren't you glad you got out of there!")

import random

highest = 10
answer = random.randint(1,highest)

print("Please pick a number between 1 and {}".format(highest))
guess = int(input())
if guess != answer:
    if guess < answer:
        print("Please guess higher.")
    else:
        print("Please guess lower.")
    guess = int(input())
    if guess == answer:
        print("Well done!")
    else:
        print("Sorry.")
else:
    print("Good job!  You guessed it on the first try.")

