file = "/home/ec2-user/environment/CPMC/FileIO/cities.txt"

cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]

with open(file, 'w') as cities_file:
    for city in cities:
        print(city, file=cities_file)

cities = []
with open(file, 'r') as cities_file:
    for city in cities_file:
        cities.append(city.strip('\n')) # strip removes from beginning or end of string, including partial matches
print(cities)
for city in cities:
    print(city)