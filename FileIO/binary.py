# file = "/home/ec2-user/environment/CPMC/FileIO/binary.file"

# with open(file, 'bw') as bin_file:
#     # for i in range(17):
#         # bin_file.write(bytes([i])) # must send value as a list; an integer would create that many zero-value bytes
#     bin_file.write(bytes(range(17)))

# with open(file, 'br') as binFile:
#     for b in binFile:
#         print(b)
    
file = "/home/ec2-user/environment/CPMC/FileIO/binary2.file"

a = 65534       # FF FE
b = 65535       # FF FF
c = 65536       # 00 01 00 00
x = 2998302     # 02 2D C0 1E

with open(file, 'bw') as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'big')) # 02 2d c0 1e
    bin_file.write(x.to_bytes(4, 'little')) # 1e c0 2d 02

with open(file, 'br') as bin_file:
    print(int.from_bytes(bin_file.read(2), 'big'))
    print(int.from_bytes(bin_file.read(2), 'big'))
    print(int.from_bytes(bin_file.read(4), 'big'))
    print(int.from_bytes(bin_file.read(4), 'big'))
    print(int.from_bytes(bin_file.read(4), 'big')) # reverse-endian