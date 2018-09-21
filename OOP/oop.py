#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 14, 2018 8:25:56 PM$"

#a = 12
#b = 4
#print(a+b)
#print(a.__add__(b))

class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on() # self parameter is populated by Python
print(hamilton.on)

print(kenwood.on)
Kettle.switch_on(kenwood) # explicit self parameter
print(kenwood.on)

kenwood.power = 1.5 # adhoc creation of a new instance variable, unique to this instance
print(kenwood.power)

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__) # no power_source
print(hamilton.__dict__) # no power_source

print(kenwood.power_source is Kettle.power_source)

kenwood.power_source = "gas"
print(kenwood.power_source)
print(Kettle.power_source)
print(kenwood.power_source is Kettle.power_source)
print(kenwood.__dict__) # now included power_source