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

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far south")

    def quack(self):
        print("Are you 'avin a larf?  I'm a penguin!")

#def test_duck(duck):
#    duck.walk()
#    duck.swim()
#    duck.quack()


if __name__ == "__main__":
    donald = Duck()
    donald.fly()
#    test_duck(donald)

#    percy = Penguin()
#    test_duck(percy)