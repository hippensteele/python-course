import random

highest = 10
answer = random.randint(1,highest)

print("Please pick a number between 1 and {}".format(highest))
guess = int(input())
if guess != answer:
    while guess != answer and guess != 0:
        if guess < answer:
           print("Please guess higher.")
        else:
            print("Please guess lower.")
        guess = int(input())
        if guess == answer:
            print("Well done!")
else:
    print("Good job!  You guessed it on the first try.")