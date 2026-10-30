from dice import Dice
from abc import ABC, abstractmethod
from race import *
import random
from attacks import *
# class char_Class:
#     def __init__(self):
#         self.weapon 



class Entity(ABC):
    def __init__(self, armour_class, race: Race, strength = (Dice(6).roll()+Dice(6).roll()+Dice(6).roll()), dexterity=(Dice(6).roll()+Dice(6).roll()+Dice(6).roll()), intelligence=(Dice(6).roll()+Dice(6).roll()+Dice(6).roll()), constitution=(Dice(6).roll()+Dice(6).roll()+Dice(6).roll()), wisdom=(Dice(6).roll()+Dice(6).roll()+Dice(6).roll()), charisma=(Dice(6).roll()+Dice(6).roll()+Dice(6).roll())):
        self.__stats = {
            'str': strength + self.get_race_bonus('str'),
            'dex': dexterity + self.get_race_bonus('dex'),
            'int': intelligence + self.get_race_bonus('int'),
            'con': constitution + self.get_race_bonus('con'),
            'wis': wisdom + self.get_race_bonus('wis'),
            'cha': charisma + self.get_race_bonus('cha')
        }

        self.__armour_class = armour_class
        self.attacklist = set() #if youre glumply like that
        self.__race = race
        # self.__char_class = char_class
        self.__health_points = 100


    #armour class property methods
    def get_armour_class(self):
        return self.__armour_class
    def set_armour_class(self, ac):
        if isinstance(ac, int):
            self.__armour_class = ac
            return ac
        else: return None
    armour_class = property(get_armour_class, set_armour_class)

    #health property methods
    def get_health_points(self):
        return self.__health_points
    def set_health_points(self, hp):
        if isinstance(hp, int):
            self.__health_points = hp
            return hp
        else: return None
    health_points = property(get_health_points, set_health_points)

    def get_race_bonus(self, stat):
        if stat in self.__race.bonuses:
            return self.__race.bonuses[stat]
        else:
            return 0


    def roll_AC(self, target):
        print('rolling to hit' + target.name)
        roll = Dice.roll(20)
        if roll >= target.stats['dex']:
            print("Hit lands")
            return True
        else:
            return False
    
    def recieve_damage(self, amount):
        self.__health_points -= amount
        return self.__health_points
        
    @abstractmethod
    def turn_method(self):
        pass

class Enemy_Entity(Entity):
    def __init__(self, race: Race):
        super().__init__(race)
    
    def turn_method(self, target):
        if self.__health_points >= 0:
            self.attacklist[random.randint(1, len(self.attacklist))].hit(self, target)

class player_entity(Entity):
    def __init__(self, race):
        super().__init__(race) 
    
    def turn_method(self, target):
        if self.__health_points >=0 :
            action = input("would you like to attack (a), or use an item (I)")
            if action.lower() == "a":
                for i, attack in enumerate(self.attacklist):
                    print(f"{i} - {attack.name}")
                attack_action = int(input("which attack would you like to use?"))
                self.attacklist[attack_action].hit(self, target)

        

