from attacks import *

class Class:
    def __init__(self, name, attacks: list = None):
        self.name = name
        if attacks is None:
            self._attacks = []
        else:
            self._attacks = attacks

    def add_attack(self, attack):
        self._attacks.append(attack)

    def get_attacks(self):
        return self._attacks
    
    attacks = property(get_attacks)
    
classes = {
    "b": Class("barbarian", [melee_atks["slash"], melee_atks["stab"]]),
    "w": Class("wizard", [rand_atks["fireball"], rand_atks["lightning bolt"]]),
    "r": Class("rogue", [melee_atks["stab"], melee_atks["dagger strike"]]),
}
