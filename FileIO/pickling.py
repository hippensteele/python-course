import pickle

file = "/home/ec2-user/environment/CPMC/FileIO/imelda.pickle"

imelda = ('More Mayhem',
          'Imelda May',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))

# with open(file, 'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file)

# with open(file, 'rb') as pickle_file:
#     imelda2 = pickle.load(pickle_file)

# # print(imelda2)
# import pprint
# pprint.pprint(imelda)

# album, artist, year, tracklist = imelda2
# print(album, artist, year, sep=', ')
# for i in tracklist:
#     track, song = i
#     print(track, song, sep=': ')

even = range(0, 10, 2)
odd = range(1, 10, 2)

with open(file, 'wb') as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=0)
    pickle.dump(even, pickle_file, protocol=4) # 3+ not readable by Python 2.x
    pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(2998302, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)

### objects must be retrieved in the same order
### protocol is detected automatically, even if different within same pickle file
with open(file, 'rb') as pickle_file:
    imelda2 = pickle.load(pickle_file)
    even2 = pickle.load(pickle_file)
    odd2 = pickle.load(pickle_file)
    x = pickle.load(pickle_file)

for i in even2:
    print(i)

