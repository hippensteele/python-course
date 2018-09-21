# string = "123456789"
# ### for loop automatically uses an iterator, and exits on the StopIteration error
# for char in string:
#     print(char)
# ### same as:
# for char in iter(string):
#     print(char)
# ### manually created iterators must handle the StopIteration error
# my_iterator = iter(string)
# print(my_iterator)
# for i in range(10):
#     print(next(my_iterator))

### mini-challenge:
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
iterator = iter(days)
for i in range(0, len(days)):
    print(next(iterator))

# ### normal way:
# for day in days:
#     print(day)