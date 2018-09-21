name = input("What is your name? ")
age = int(input("How old are you, {}? ".format(name)))

if 18 <= age <= 30:
    print("Hello {}, welcome to the holiday!".format(name))
else:
    print("Sorry {}, this is an 18-30 holiday.".format(name))