import shelve

with shelve.open("./CPMC/FileIO/motorcycle.shelf") as bike:
    # bike["make"] = "Honda"
    # bike["model"] = "250 Dream"
    # bike["colour"] = "red"
    # bike["engine_size"] = 250
    # bike["engin_size"] = 250
    # del bike["engin_size"]
    for key in bike:
        print(key, bike[key], sep=': ')