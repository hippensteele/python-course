#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 28, 2018 4:02:37 PM$"

burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans", "spam"]

meals = [(burger, topping) for burger in burgers for topping in toppings]
print(meals)

print()

for burger in burgers:
    for topping in toppings:
        print((burger, topping))

print()

for meal in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meal)

print()

for meal in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(meal)

print('*' * 40)

for i in range(1, 11):
    for j in range(1, 11):
        print(i, i*j)

times_table = [(i, i * j) for i in range(1,11) for j in range(1,11)]
print(times_table)

print("List comprehension:")

for x, y in [(i, i * j) for i in range(1,11) for j in range(1, 11)]:
    print(x, y)

print("Generator function syntax uses less memory:")

for x, y in ((i, i * j) for i in range(1,11) for j in range(1, 11)):
    print(x, y)