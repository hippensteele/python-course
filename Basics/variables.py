# ### variables must start with letters or underscores
# greeting = "Bruce"
# _123 = "numbers"
# ## 123 = "new new numbers" # syntax error

# ### + won't cast number to char
# age = 52
# ### print(greeting + age) # syntax error
# print(greeting + _123)

# a = 12
# b = 3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b) # returns a float
# print(a//b) # returns an integer
# print(a % b)

# for i in range(1, a//b): # requires an int
#     print(i)

parrot = "Norwegian Blue"
# print(parrot)
# print(parrot[3])
# print(parrot[0])
# print(parrot[-1])
# print(parrot[0:6])
# print(parrot[:6])
# print(parrot[6:])
print(parrot[-4:-2])
# print(parrot[0:6:2]) # steps of 2
# print(parrot[0:6:3]) # steps of 3

# number = "1,123,123,123,123,123"
# print(number[1::4])
# numbers = "1, 2, 3, 4, 5"
# print(numbers[0::3])

print("Hello " * 5)

today = "friday"
print('day' in today)
print("thu" in today)