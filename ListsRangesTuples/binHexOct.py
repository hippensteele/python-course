# for i in range(256):
#     print("{0:>2} is {0:>08b} in binary".format(i))
# for i in range(17):
#     print("{0:>2} is {0:>02x} in hex".format(i))
    
# x = 0x20
# y = 0x0a
# print(x)
# print(y)
# print(x*y)

# print(0b00101010)

### challenge

dec = int(input("Please type a number: "))

base = 2
max = 0
result = "" 

for i in range(32):
    if (dec // (base ** i)) == 0:
        max = i
        break
max -= 1 

wrk = dec    
for i in range(max,-1,-1):
    w = wrk//(base**i)
    if w > 0:
        result += '1'
        wrk -= (w * (base**i))
    else:
        result += '0'

print("{0:>3} is {1} in binary.".format(dec,result))
    
### answer:
powers = []

for power in range(15,-1,-1):
    powers.append(2**power)

x = dec
printing = False
for power in powers:
    bit = x // power
    if bit != 0 or power == 1:
        printing = True
    if printing:
        print(bit,end='')
    x %= power



