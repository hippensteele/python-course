#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 18, 2018 5:52:01 AM$"

import random

class Enemy:  # same as "class Enemy(object)"; superclass is object
    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self._original_hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("I took {} points damage and have {} left.".format(damage, self.hit_points))
        else:
            self.lives -= 1
            self.hit_points = self._original_hit_points
            if self.lives > 0:
                print("{0.name} lost a life".format(self))
            else:
                self.alive = False
                print("{0.name} is dead".format(self))

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit points: {0.hit_points}".format(self)


class Troll(Enemy): # subclass of Enemy

    def __init__(self, name="Troll", hit_points=0, lives=1):
        super().__init__(name, hit_points, lives)

    def grunt(self):
        print("Me {0.name}, {0.name} stomp you".format(self))


class Vampyre(Enemy):

    def __init__(selfself, name="Fang", hit_points=12, lives=3):
        super().__init__(name, hit_points, lives)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("***** {0.name} dodges *****".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)

class VampyreKing(Vampyre):

    def __init__(self, name="BigFang"):
        super().__init__(name=name, hit_points=140)

    def take_damage(self, damage):
        split_damage = damage // 4
        if split_damage > 0:
            super().take_damage(damage=split_damage)
        else:
            super().take_damage(damage=1)
