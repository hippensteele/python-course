
# jabber = open("/home/ec2-user/environment/CPMC/FileIO/sample.txt",'r')
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
# jabber.close()

### no need to close the file after, if using with
file = "/home/ec2-user/environment/CPMC/FileIO/sample.txt"
# with open (file, 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open(file, 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# with open(file, 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
# print(''.join(lines))
# for line in lines:
#     print(line, end='')

with open(file, 'r') as jabber:
    lines = jabber.readlines()
for line in lines[::-1]:
    print(line, end='')
    
with open(file, 'r') as jabber:
    lines = jabber.read()
for line in lines[::-1]:
    print(line, end='')