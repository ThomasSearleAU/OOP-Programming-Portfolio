from dice import Dice
from abc import ABC, abstractmethod
class char_Class:
    def __init__(self):
        self.weapon 

class Race:
    def __init__(self, name, speed, abilities):
        self.name = name
        self.speed = speed
        self.abilities = abilities

class Entity(ABC):
    def __init__(self, race: Race, char_class: char_Class, strength, dexterity, intelligence, constitution, wisdom, charisma):
        self.__stats = {
            'str': strength + self.get_race_bonus('str'),
            'dex': dexterity + self.get_race_bonus('dex'),
            'int': intelligence + self.get_race_bonus('int'),
            'con': constitution + self.get_race_bonus('con'),
            'wis': wisdom + self.get_race_bonus('wis'),
            'cha': charisma + self.get_race_bonus('cha')
        }
        self.attacklist = {
            'Unarmed Strike': [5 * self.stats['str'], 'melee']
        }
        self.__race = race
        self.__char_class = char_class


    def roll_AC(self, target):
        print('rolling to hit' + target.name)
        roll = Dice.roll(20)
        if roll >= target.stats['dex']:
            print("Hit lands")
            return True
        else:
            return False
    
    def recieve_damage(self, amount):
        self.__health_points
        
    @abstractmethod
    def combat_turn(self):
        pass
        #according to d&d handbook, combat turns look like the following:
        #1. movement - not really sure if it is compatible, seeing as my fight engine is more just turn based, and not simulated in a 'space'
        #2. initiative should determine who's turn goes first
        #use One action -i guess if playing barbarian add class action for 



class Enemy_Entity:
    def combat_turn(self):
        hit = self.roll_AC(target)
        if hit:
            