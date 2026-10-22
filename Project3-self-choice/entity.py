
class char_Class:
    pass

class Race:
    def __init__(self, name, speed, abilities):
        self.name = name
        self.speed = speed
        self.abilities = abilities

class Entity():
    def __init__(self, race: Race, char_class: char_Class, strength, dexterity, intelligence, constitution, wisdom, charisma):
        self.stats = {
            'str': strength + self.get_race_bonus('str'),
            'dex': dexterity + self.get_race_bonus('dex'),
            'int': intelligence + self.get_race_bonus('int'),
            'con': constitution + self.get_race_bonus('con'),
            'wis': wisdom + self.get_race_bonus('wis'),
            'cha': charisma + self.get_race_bonus('cha')
        }
        self.race = race
        self.char_class = char_class