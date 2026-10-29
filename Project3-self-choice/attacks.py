from abc import ABC, abstractmethod
import random
from dice import *
class Attack(ABC):
    def __init__(self, dice, name, type):
        self.__dmg_dice = dice
        self.__name = name
        self.__type = type
    
    @abstractmethod
    def hit(self, caller, target):
        pass

class Magic_Attack(Attack):
    def hit(self, caller, target, dice_quantity, dice_sides):
        roll = random.randint(1, 20)
        if roll >= target.armour_class:
            dmg = 0
            for i in range(dice_quantity):
                dmg += Dice(dice_sides).roll
            dmg += caller.__stats[self.__dmg_stat]
        





# class Magic_Attack(Attack):
#     def __init__(self, dice, effect, element):
#         pass