import random

from attacks import *
from dice import *
from entity import *
from race import *
from class_ import *
clearer = "\033[H\033[2J\033[3J"
class Game:
    def __init__(self, player: player_entity):
        self.player = player
        self.enemies = [
            Orc_Enemy(),
            Goblin_Enemy(),
            Skeleton_Enemy()
        ]   

            #player = Entity(race, classe, stre, dex, inte, const, wis, char)

    def Game_Method(self):
        
        Game = True
        wins = 0
        while Game:
            enemy = random.choice(self.enemies)
            print(f"You are facing a: {enemy.__class__.__name__}")
            turn = 0
            while self.player.health_points > 0 and enemy.health_points > 0:
                turn += 1
                input(f"round: {turn}, you are have: {self.player.health_points} HP. enemy has {enemy.health_points} HP.")
                input("Your Turn. (enter to continue)")
                print(clearer)
                self.player.turn_method(enemy)
                input("Enemy's Turn. (enter to continue)")
                print(clearer)
                enemy.turn_method(self.player)
            if self.player.health_points <= 0:
                Game = False
            else: 
                print("the enemy has been slain!")
                wins += 1

        # while player.health_points > 0:
        #     enemy = random.choice(self.enemies)
        #     if enemy.health_points > 0:
        #         player.turn_method(enemy)
        #         enemy.turn_method(player)
if __name__ == '__main__':
    print(clearer)
    x = input("what race [H - human, E - Elf, O - Orc]: ").upper()
    print(clearer)
    race = races[x]
    # print(f"{race.name}")

    y = input("what class [B - barbarian, W - wizard, R - rogue]").upper()
    print(clearer)
    class_ = classes[y]

    player = player_entity(race, class_)
    game = Game(player)
    
    game.Game_Method()


