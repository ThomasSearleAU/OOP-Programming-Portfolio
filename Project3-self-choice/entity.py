from dice import Dice
from abc import ABC, abstractmethod
from race import *
import random
from attacks import *
# class char_Class:
#     def __init__(self):
#         self.weapon 
import math


from class_ import * 
class Entity(ABC):
    def __init__(self, race: Race, class_: Class, strength = (Dice(6).roll()+Dice(6).roll()+Dice(6).roll()), dexterity=(Dice(6).roll()+Dice(6).roll()+Dice(6).roll()), intelligence=(Dice(6).roll()+Dice(6).roll()+Dice(6).roll()), constitution=(Dice(6).roll()+Dice(6).roll()+Dice(6).roll()), wisdom=(Dice(6).roll()+Dice(6).roll()+Dice(6).roll()), charisma=(Dice(6).roll()+Dice(6).roll()+Dice(6).roll())):
        self.race = race
        self.class_ = class_
        self.__stats = {
            'str': strength + self.get_race_bonus('str'),
            'dex': dexterity + self.get_race_bonus('dex'),
            'int': intelligence + self.get_race_bonus('int'),
            'con': constitution + self.get_race_bonus('con'),
            'wis': wisdom + self.get_race_bonus('wis'),
            'cha': charisma + self.get_race_bonus('cha')
        }

        self.__armour_class = math.floor((self.__stats['dex']-10)/2) + 10
        self.class_ = class_
        
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

    def get_stats(self):
        return self.__stats
    
    stats = property(get_stats)

    def get_race_bonus(self, stat):
        if stat in self.race.bonuses:
            return self.race.bonuses[stat]
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

#-----------------------------------Enemy classes-----------------------------------#

class Enemy_Entity(Entity):
    def __init__(self, race: Race, class_):
        super().__init__(race, class_)
        # self.item_to_drop               -implement
    
    def turn_method(self, target):
        if self.health_points >= 0:
            # self.class_.attacks[random.randint(0, len(self.class_.attacks))].hit(self, target)
            random.choice(self.class_.attacks).hit(self, target)

class Orc_Enemy(Enemy_Entity):
    def __init__(self):
        super().__init__(orc_race, classes["B"])
        self.health_points = 200

class Goblin_Enemy(Enemy_Entity):
    def __init__(self):
        super().__init__(goblin_race, classes["R"])
        self.health_points = 85

class Skeleton_Enemy(Enemy_Entity):
    def __init__(self):
        super().__init__(skeleton_race, classes["W"])
        self.health_points = 90


#-----------------------------------Player class-----------------------------------#
clearer = "\033[H\033[2J\033[3J"
class player_entity(Entity):
    def __init__(self, race, class_):
        super().__init__(race, class_)
        self.inventory = []
        
    
    def turn_method(self, target):
        if self.health_points >=0 :
            while True:
                action = input("would you like to attack (a), or use an item (I)")
                print(clearer)
                if action.lower() == "a":
                    for i, attack in enumerate(self.class_.attacks):
                        print(f"{i} - {attack.name}")
                    if len(self.class_.attacks) > 0:
                        attack_action = (input("which attack would you like to use? [type 'esc' to go back]: "))
                        if attack_action.strip().lower() == "esc": 
                            print(clearer)
                            continue
                        
                        else: 
                            attack_action = int(attack_action)

                        self.class_.attacks[attack_action].hit(self, target)
                        break
                    else:
                        print("No attacks in list.")
                elif action.lower() == "i":
                    if len(self.inventory) > 0:
                        for i, item in enumerate(self.inventory):
                            print(f"{i} - {item.name}\n")
               
                        item_sel = self.inventory[int(input("which item (by index): "))]
                        item_sel.use_item
                       
                           
                        break
                    else:
                        print("No items in inventory")
        

