fruit = { "orange": "a sweet, orange, citrus fruit",
          "apple": "good for making cider",
          "lemon": "a sour, yellow, citrus fruit",
          "grape": "a small, sweet fruit growing in bunches",
          "lime": "a sour, green, citrus fruit"}
# print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "an odd-shaped apple"
# print(fruit)
# fruit["lime"] = "great with tequila"
# print(fruit)

# del fruit["lemon"]
# print(fruit)
# fruit.clear()
# print(fruit)

# print(fruit["tomato"])

# while True:
#     dict_key = input("Please type a fruit name: ")
#     if dict_key == "quit":
#         break
#     # if dict_key in fruit:
#     #     description = fruit.get(dict_key) # get() returns None if the key is not found
#     #     print(description)
#     # else:
#     #     print("We don't have " + dict_key)
#     description = fruit.get(dict_key, "We don't have " + dict_key) # default value
#     print(description)

# for snack in fruit:
#     print(snack)
#     print('\t' + fruit[snack])

### order of keys can change depending on memory position when hashed (never replicated with this test)
# keyOrderSave = ""
# for i in range(10000):
#     # del fruit
#     # fruit.clear()
#     # fruit = { "orange": "a sweet, orange, citrus fruit",
#     #       "apple": "good for making cider",
#     #       "lemon": "a sour, yellow, citrus fruit",
#     #       "grape": "a small, sweet fruit growing in bunches",
#     #       "lime": "a sour, green, citrus fruit"}
#     del fruit["lemon"]
#     fruit["lemon"] = "a sour, yellow, citrus fruit"
#     keyOrder = ""
#     for snack in fruit:
#         keyOrder += snack + " "
#     if keyOrder != keyOrderSave:
#         print(keyOrder)
#         keyOrderSave = keyOrder

### to get consistent ordering:
## ordered_list = list(fruit.keys())
## ordered_list.sort()
# ordered_list = sorted(list(fruit.keys()))
# for f in ordered_list:
#     print(f + " - " + fruit[f])
# for f in sorted(fruit.keys()):
#      print(f + " - " + fruit[f])
# ### iterating over values is less efficient than by keys
# for val in fruit.values():
#     print(val)
    
### tuple from dictionary:
f_tuple = tuple(fruit.items())
for snack in f_tuple:
    item, description = snack
    print(item + ": " + description)
### dictionary from tuple:
print(dict(f_tuple))