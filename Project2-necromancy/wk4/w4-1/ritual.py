class Ritual:
    def __init__(self, undead_name, ritual_name, init_health, init_power, necrotic_rune, spirit_rune, bone_rune, flesh_rune, ectoplasm):
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
    