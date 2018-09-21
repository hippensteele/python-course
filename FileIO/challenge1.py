file = "/home/ec2-user/environment/CPMC/FileIO/multiplicationTables.txt"

with open(file, 'a') as multTbl: # 'a' means append
    for i in range(1, 13):
        for j in range(1, 13):
            print("{0:>2} times {1:>2} is {2:>3}".format(i, j, i * j), file=multTbl)
        print('-' * 18, file=multTbl)