locations = {0: "You are sitting at a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}
synonyms = {"WEST":"W", "EAST": "E", "SOUTH": "S", "NORTH": "N", "QUIT": "Q"}

# print(locations[0].split())
# print(locations[3].split(","))
# print(' '.join(locations[0].split()))

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])
    if loc == 0:
        break
    direction = input("Available exits are " + availableExits + ": ").upper()
    # if direction in synonyms: # this requires the exact word
    #     direction = synonyms[direction]
    if len(direction) > 1:
        # for word in synonyms: # this allows "go west", etc.
        #     if word in direction:
        #         direction = synonyms[word]
        words = direction.split()
        for word in words:
            if word in synonyms:
                direction = synonyms[word]
                break
                
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You can't go that way.")