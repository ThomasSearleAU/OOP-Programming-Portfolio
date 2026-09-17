from inventory import Inventory
from undead import *
import random
class Ritual:
    def __init__(self,  type: Undead, undead_name, ritual_name, necrotic_rune=0, spirit_rune=0, bone_rune=0, flesh_rune=0, ectoplasm=1):
        self.undead_name = undead_name
        self.ritual_name = ritual_name
        # self.init_health = init_health
        # self.init_power = init_power
        #commented above because i am not sure how to get the elements of an object before instantiating. 
        #if added back, remember to add params

        self.unit_id_setter = 0
        self.costs = {
            'Necrotic Rune': necrotic_rune,
            'Spirit Rune': spirit_rune,
            'Bone Rune': bone_rune,
            'Flesh Rune': flesh_rune,
            'Ectoplasm': ectoplasm
        }
        self.type = type

    def check_requirements(self, inventory: Inventory):
        return inventory.check_requirements(self.costs)

    def summon_undead(self, inventory):
        inventory.spend_ritual_cost(self)
        return self.type(self.unit_id_setter, self.type.NAME, str(self.type))
        self.unit_id_setter += 1

# class DeathKnightRitual_(Ritual):   # i did this accidentally cos i am schtoopeed
#     def __init__(self):
#         super().__init__("", "DeathKnightRitual", 99,99,99,99,99)
#     def summon_undead(self, inventory, name, hp, pwr, type):
#         inventory.spend_ritual_cost(self)
#         if random.randint(1, 4) == 1:
#             return DeathKnight(self.unit_id_setter, "Death Knight", name, hp, pwr, type)
#         else:
#             print("summon failed!")

# inventory = Inventory()
# DeathKnightRitual = Ritual("DeathKnight", "DeathKnightRitual", 99,99,99,99,99, DeathKnight) #this is how it was asked