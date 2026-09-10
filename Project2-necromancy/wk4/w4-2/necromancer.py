from inventory import Inventory
from undead import Undead
from ritual import Ritual
class Necromancer:
    MAX_UNDEAD = 10
    def __init__(self, name):
        self.__name = name
        self.__inventory = Inventory()
        self.__undead_list = []

    def summon_undead(self, ritual):
        if len(self.__undead_list) >= self.MAX_UNDEAD:
            print(f"Cannot summon more undead. Maximum limit of {self.MAX_UNDEAD} reached.")
            return None

        if not ritual.check_requirements(self.__inventory):
            print("Not enough resources to perform the ritual.")
            return None

        self.__inventory.spend_ritual_cost(ritual.costs)
        new_undead = Undead(len(self.__undead_list) + 1, ritual.undead_name, ritual.init_health, ritual.init_power)
        self.__undead_list.append(new_undead)
        print(f"Summoned {new_undead}")
        return new_undead

    