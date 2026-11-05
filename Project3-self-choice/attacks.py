from abc import ABC, abstractmethod
import random
from dice import *
class Attack(ABC):
    def __init__(self, dice_quantity, dice_sides, name, type):
        self._dice_quantity = dice_quantity
        self._dice_sides = dice_sides
        self._name = name
        self._type = type

    @abstractmethod
    def hit(self, caller, target):
        pass

class Magic_Attack(Attack):
    def hit(self, caller, target):
        print(f"{caller.name}")
        roll = random.randint(1, 20)
        if roll >= target.armour_class:
            print(f"{self._name}, has hit the target!")
            dmg = 0
            for i in range(self._dice_quantity):
                dmg += Dice(self._dice_sides).roll
            dmg += caller._stats['wis']
            return True
        else:
            print(f"{self._name}, failed.")
            return False

class Melee_Attack(Attack):
    def hit(self, caller, target):
        print(f"{caller.name}")
        roll = random.randint(1, 20)
        if roll >= target.armour_class:
            print(f"{self._name}, has hit the target!")
            dmg = 0
            for i in range(self._dice_quantity):
                dmg += Dice(self._dice_sides).roll
            dmg += caller._stats['str']
            return True
        else:
            print(f"{self._name}, failed.")
            return False

rand_atks = {
    "fireball": Magic_Attack(3, 6, "Fireball", "magic"),
    "lightning bolt": Magic_Attack(3, 6, "Lightning Bolt", "magic"),
    "ice shard": Magic_Attack(2, 8, "Ice Shard", "magic"),
    "acid splash": Magic_Attack(2, 6, "Acid Splash", "magic"),
    "magic missile": Magic_Attack(1, 10, "Magic Missile", "magic"), 
    "poison dart": Magic_Attack(1, 8, "Poison Dart", "magic"),
}

melee_atks = {
    "slash": Melee_Attack(2, 8, "Slash", "melee"),
    "stab": Melee_Attack(2, 6, "Stab", "melee"),
    "whack": Melee_Attack(1, 12, "Whack", "melee"),
    "stomp": Melee_Attack(1, 10, "Stomp", "melee"),
    "punch": Melee_Attack(1, 8, "Punch", "melee"),
    "sword strike": Melee_Attack(2, 10, "Sword Strike", "melee"),
    "dagger strike": Melee_Attack(1, 6, "Dagger Strike", "melee"),
    "axe chop": Melee_Attack(2, 12, "Axe Chop", "melee"),
}



# class Magic_Attack(Attack):
#     def __init__(self, dice, effect, element):
#         pass