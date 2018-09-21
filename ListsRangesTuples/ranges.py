# print(range(10))
# my_list = list(range(10))
# print(my_list)

# even = list(range(0,10,2))
# odd = list(range(1,10,2))
# print(even)
# print(odd)

# my_string = "abcdefghijklmnopqrstuvwxyz"
# print(my_string.index('e'))
# print(my_string[4])

# small_decimals = range(10)
# print(small_decimals)
# print(small_decimals.index(3))
# print(small_decimals.index(0))

# odd = range(1,10000,2)
# print(odd[985])

# sevens = range(7,100000,7)
# number = int(input("Please enter a number: "))
# if number in sevens:
#     print("{} is divisible by 7".format(number))

# small_decimals = range(10)
# my_range = small_decimals[::2]
# print(my_range)
# print(my_range[4])
# print(my_range.index(8))
# print(my_range.index(3))

# decimals = range(100)
# print(decimals)
# my_range = decimals[3:40:3]
# print(my_range)

# for i in my_range:
#     print(i,end=' ')
# print('\n' + "=" * 40)
# for i in range(3,40,3):
#     print(i, end=' ')

# print(my_range == range(3,40,3))

# print(range(0,5,2) == range(0,6,2))
# print(list(range(0,5,2)))
# print(list(range(0,6,2)))

# r = range(100)
# for i in r[::-2]:
#     print(i,end=' ')
# print()
# for i in range(99,0,-2):
#     print(i,end=' ')

print(range(0,100)[::-2] == range(99,0,-2))

backString = "esrever"
print(backString[::-1])
r = range(10)
for i in r[::-1]:
    print(i)
