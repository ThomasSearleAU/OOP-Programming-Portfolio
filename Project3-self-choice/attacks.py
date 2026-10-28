
class Attack:
    def __init__(self, dice):
        self.__dmg_dice = dice

class Melee_Attack(Attack):
    def __init__(self, dice, type, bleed, stam_cost):
        super().__init__(dice)
        self.__atk_type = type
        self.__bleed = bleed
        self.__stamina_cost = stam_cost

class Magic_Attack(Attack):
    def __init__(self, dice, effect, element):
        