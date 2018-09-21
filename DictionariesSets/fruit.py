fruit = { "orange": "a sweet, orange, citrus fruit",
          "apple": "good for making cider",
          "lemon": "a sour, yellow, citrus fruit",
          "grape": "a small, sweet fruit growing in bunches",
          "lime": "a sour, green, citrus fruit" }
# print(fruit)
veg = { "cabbage": "every child's favorite",
        "sprouts": "mmmmm, lovely",
        "spinach": "can I have some more fruit, please?" }
# print(veg)

# veg.update(fruit) # adds fruit to the veg dictionary
# print(veg)

### to make a new dictionary combining both, use copy and then update
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)