
#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 16, 2018 5:33:01 AM$"

#from player import Player
#tim = Player("Tim")
#print(tim.name)
#print(tim.lives)
#tim.lives -= 10
#print(tim.lives)
#print(tim)
#print('*' * 20)
#tim.level = 3
#print(tim)
#tim.level -= 2
#print(tim)
#tim.level = 2
#print(tim)
#tim.level -= 3
#print(tim)
#tim.score += 100
#print(tim)

from enemy import Enemy, Troll, Vampyre, VampyreKing

#random_monster = Enemy("Basic enemy", 12, 1)
#print(random_monster)
#random_monster.take_damage(4)
#print(random_monster)
#random_monster.take_damage(8)
#print(random_monster)
#random_monster.take_damage(9)
#print(random_monster)

#ugly_troll = Troll()
#print("Ugly troll - {}".format(ugly_troll))
#
#another_troll = Troll("ug", 18, 1)
#print("Another troll - {}".format(another_troll))
#
#brother = Troll("Urg", 23)
#print(brother)
#brother.grunt()
#brother.take_damage(5)

vamp = Vampyre("Vlad")
while vamp.alive:
    vamp.take_damage(1)
#    print(vamp)

vampTheGreat = VampyreKing("Big Vlad")
while vampTheGreat.alive:
    vampTheGreat.take_damage(8)

