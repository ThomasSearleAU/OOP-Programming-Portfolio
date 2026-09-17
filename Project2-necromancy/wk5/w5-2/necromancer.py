from inventory import Inventory
from undead import Undead
from ritual import Ritual
class Necromancer:
    MAX_UNDEAD = 10
    def __init__(self, name, type):
        self.__name = name
        self.__inventory = Inventory()
        self.__undead_list= []
        self.__undead_type = type

    def summon_undead(self, ritual):
        if len(self.__undead_list) >= self.MAX_UNDEAD:
            print(f"Cannot summon more undead. Maximum limit of {self.MAX_UNDEAD} reached.")
            return None

        if not ritual.check_requirements(self.__inventory):
            print("Not enough resources to perform the ritual.")
            return None
        self.__undead_list.append(ritual.summon_undead())

    def dismiss_undead(self, id):
        for individual in self.__undead_list:
            if individual.get_id() == id:
                self.__undead_list.pop(individual) 