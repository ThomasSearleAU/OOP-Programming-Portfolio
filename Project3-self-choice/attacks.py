from abc import ABC, abstractmethod
import random
from dice import *
class Attack(ABC):
    def __init__(self, dice_quantity, dice_sides, name, type):
        self.__dice_quantity = dice_quantity
        self.__dice_sides = dice_sides
        self.__name = name
        self.__type = type
    
    @abstractmethod
    def hit(self, caller, target):
        pass

class Magic_Attack(Attack):
    def hit(self, caller, target):
        print(f"{caller.name}")
        roll = random.randint(1, 20)
        if roll >= target.armour_class:
            print(f"{self.__name}, has hit the target!")
            dmg = 0
            for i in range(self.__dice_quantity):
                dmg += Dice(self.__dice_sides).roll
            dmg += caller.__stats[self.__dmg_stat]
            return True
        else:
            print(f"{self.__name}, failed.")
            return False





# class Magic_Attack(Attack):
#     def __init__(self, dice, effect, element):
#         pass