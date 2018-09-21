# farm_animals = {"sheep", "cow", "hen" }
# for animal in farm_animals:
#     print(animal)
# print("=" * 40)

# wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
# for animal in wild_animals:
#     print(animal)
# print("=" * 40)

# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

# ### much use set function to create an empty set
# empty_set = set([])
# empty_set2 = {}
# empty_set.add("item")
#  # empty_set2.add("item") # errors out

# even = set(range(0,40,2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)

even = set(range(0,40,2))
print(even)
print(len(even))
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(len(squares))

print(even.union(squares))
print(len(even.union(squares)))

print("-" * 40)

print(even.intersection(squares))
print(even & squares)

print("-" * 40)

print(sorted(even))
print(sorted(squares))

print(sorted(even.difference(squares)))
print(sorted(even - squares))
print(sorted(squares.difference(even)))
print(sorted(squares - even))

print("-" * 40)

print(sorted(even))
print(squares)
even.difference_update(squares)
print(even)

print("-" * 40)

even = set(range(0,40,2))
print(sorted(even))
squares = {4, 6, 9, 16, 25}
print(sorted(squares))
### opposite of intersection
print(sorted(even.symmetric_difference(squares)))
print(sorted(even ^ squares))

print("-" * 40)

print(squares)
squares.discard(4) # no error if not found
squares.remove(16) # errors if not found
squares.discard(8) # no error if not found
if 8 in squares:
    squares.remove(8)
try:
    squares.remove(8)
except KeyError:
    print("8 is not a member of the set.")
print(squares)

print("-" * 40)

even = set(range(0,40,2))
squares = {4, 6, 16}

if squares.issubset(even):
    print("squares is a subset of even")
if even.issuperset(squares):
    print("even is a superset of squares")

even = frozenset(range(0,100,2))
print(even)
