
# for i in range(1,20): # does not include 20
#     print("i is now: {}".format(i))
    
# numbers = "0123456789"
# for i in range(0,len(numbers)): # len() is 10
#     print(numbers[i])

# numbers = "0,123,456,789"
# cleanedNumber = ""
# for i in range(0,len(numbers)): # len() is 10
#     if numbers[i] in "0123456789":
#         # print(numbers[i],end='')
#         cleanedNumber += numbers[i]
# newNumber = int(cleanedNumber)
# print("The new number is {}".format(newNumber))


# numbers = "0,123,456,789"
# digits = "0123456789"
# cleanedNumber = ""
# for char in numbers:
#     if char in digits:
#         cleanedNumber += char
# newNumber = int(cleanedNumber)
# print("The number is {}".format(newNumber))

# for month in ("January","February","March"):
#     print("The month of "+month)
    
# for number in range(0,100,5):
#     print(number,end=' ')

for i in range(1,13):
    for j in range(1,13):
        print("{0:2} times {1:2} is {2:3}".format(i,j,i*j))
    print("==================")