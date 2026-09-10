from inventory import Inventory
class Ritual:
    def __init__(self, undead_name, ritual_name, init_health, init_power, necrotic_rune=0, spirit_rune=0, bone_rune=0, flesh_rune=0, ectoplasm=1):
        self.undead_name = undead_name
        self.ritual_name = ritual_name
        self.init_health = init_health
        self.init_power = init_power
        self.costs = {
            'Necrotic Rune': necrotic_rune,
            'Spirit Rune': spirit_rune,
            'Bone Rune': bone_rune,
            'Flesh Rune': flesh_rune,
            'Ectoplasm': ectoplasm
        }

    def check_requirements(self, inventory: Inventory):
        return inventory.check_requirements(self.costs)
    
