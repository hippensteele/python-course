# t = "a", "b", "c" # a tuple
# print(t)
# print("a", "b", "c") # comma-separate values
# print(("a","b","c")) # a tuple

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

# print(metallica)
# print(metallica[0], metallica[1], metallica[2])
# ### metallica[0] = "Master of Puppets" # tuples do not support assignment; they are immutable
# ### can recreate with changes:
# print(imelda)
# imelda = imelda[0], "Imelda May", imelda[2]
# print(imelda)

# ### lists are directly mutable
# metallica2 = ["Ride the Lightning", "Metallica", 1984]
# print(metallica2)
# metallica2[0] = "Master of Puppets"
# print(metallica2)

# ### "unpacking the tuple":
# artist, title, year = imelda
# print(artist)
# print(title)
# print(year)

# imelda = "More Mayhem", "Imelda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
# print(imelda)
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# print(tracks)

# imelda = "More Mayhem", "Imelda May", 2011, (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
# title, artist, year, track1, track2, track3, track4 = imelda
# print(track1)
# print(track2)
# print(track3)
# print(track4)

# ### challenge:
# imelda = "More Mayhem", "Imelda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
# title, artist, year, tracks = imelda
# print(title + ", " + artist + ", " + str(year) + ":")
# for i in tracks:
#     print("\t{}. {}".format(i[0],i[1]))

### mutable items (lists) inside tuples remain mutable:
imelda = "More Mayhem", "Imelda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])
imelda[3].append((5, "All for You"))
title, artist, year, tracks = imelda
tracks.append((6, "Eternity"))
print(title + ", " + artist + ", " + str(year) + ":")
for i in tracks:
    track, song = i 
    print("\t{}. {}".format(track, song))
 
