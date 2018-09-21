#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 21, 2018 6:49:49 AM$"


class Wing():

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck():

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water is lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin():

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far south")

    def quack(self):
        print("Are you 'avin a larf?  I'm a penguin!")

    def aviate(self):
        print("I won the lottery and bought a learjet")

class Mallard(Duck):

    def fly(self):
        print("Mallard flying")

class Flock():

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None: # hints for the parameter type and return type
##        if type(duck) is Duck: # doesn't work: duck subtypes aren't Duck types
#        if isinstance(duck, Duck): # this works, but the real question is whether or not the object has a callable 'fly' method
        fly_method = getattr(duck, 'fly', None)
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("Cannot add that duck; are you sure it's not a " + str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError as e:
                print("One duck down: " + str(e))
                problem =  e # save the error so the loop can try to complete
#                raise
        if problem:
            raise problem

if __name__ == "__main__":
    flock = Flock()
    for i in range(10):
        flock.add_duck(Duck())
    flock.add_duck(Mallard())
    flock.add_duck(Penguin())
    flock.migrate()

