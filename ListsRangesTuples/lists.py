# ipAddress = input("Please type in an IP addres: ")
# print(ipAddress.count('.'))

# parrot_list = ["not pinin","no more","a stiff","bereft of life"]
# parrot_list.append("A Norwegian Blue")
# for state in parrot_list:
#     print("This parrot is "+state)

# even = [2,4,6,8]
# odd = [1,3,5,7]
# numbers = even + odd
# print(numbers)
# ### create a sorted copy:
# numbers_in_order = sorted(numbers)
# print(numbers_in_order)
# print("numbers and numbers_in_order are equal? " + str(numbers == numbers_in_order))
# ### sort the list in place:
# numbers.sort() # does NOT return the sorted object; can't do print(numbers.sort()); have to use sorted(numbers)
# print(numbers)
# print("numbers and numbers_in_order are equal? " + str(numbers == numbers_in_order))

# list_1 = []
# list_2 = list()
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
# print("list_1 is equal to list_2: " + str(list_1 == list_2))

# print("Assignment of lists works by reference:")
# even = [2, 4, 6, 8]
# another_even = even # pointer to same list
# print("even and another_even are the same object: " + str(another_even is even))
# another_even.sort(reverse=True)
# print("even: " + str(even))
# even.sort()
# print("another_even: " + str(another_even))
# print("But the list constructor makes a copy:")
# even = [2, 4, 6, 8]
# another_even = list(even) # new copy
# print("even and another_even are the same object: " + str(another_even is even))
# another_even.sort(reverse=True)
# print("even: " + str(even))
# even.sort()
# print("another_even: " + str(another_even))


# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7]
# numbers = [even, odd]
# for number_set in numbers:
#     print(number_set)
#     for value in number_set:
#         print(value)

menu = []
menu.append(["egg","spam","bacon"])
menu.append(["egg","sausage","bacon"])
menu.append(["egg","spam"])
menu.append(["egg","bacon","spam"])
menu.append(["egg","bacon","sausage","spam"])
menu.append(["spam","bacon","sausage","spam"])
menu.append(["spam","egg","spam","spam","bacon","spam"])
menu.append(["spam","egg","sausage","spam"])

for meal in menu:
    if "spam" not in meal:
        print(meal)
for meal in menu:
    if not "spam" in meal:
        print(meal)
        
print("Challenge:")
for meal in menu:
    if "spam" not in meal:
        for item in meal:
            print(item)