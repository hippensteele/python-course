import shelve

# with shelve.open("./CPMC/FileIO/ShelfTest.shelf") as fruit:
#     # fruit['orange'] = "a sweet, orange fruit"
#     # fruit['apple'] = "good for making cider"
#     # fruit['lemon'] = "a sour, yellow fruit"
#     # fruit['grape'] = "a sweet fruit, grows in bunches"
#     # fruit['lime'] = "a sour, green fruit"
#     print(fruit['apple'])
#     print(fruit['orange'])
# print(fruit)
# fruit.close()

fruit = shelve.open("./CPMC/FileIO/ShelfTest.shelf")
# fruit['orange'] = "a sweet, orange fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "a sour, yellow fruit"
# fruit['grape'] = "a sweet fruit, grows in bunches"
# fruit['lime'] = "a sour, green fruit"

# for snack in fruit:
#     print(snack + ": " + fruit[snack])

# while True:
#     shelf_key = input("Please choose a fruit: ")
#     if shelf_key == "quit":
#         break
#     # print(fruit.get(shelf_key, "We don't have that."))
#     if shelf_key in fruit:
#         print(fruit[shelf_key])
#     else:
#         print("We don't have a " + shelf_key)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

for v in fruit.values():
    print(v)
print(fruit.values())

for i in fruit.items():
    print(i)
print(fruit.items())


fruit.close()