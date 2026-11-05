import random

from attacks import *
from dice import *
from entity import *
from race import *
from class_ import *

class Game:
    def __init__(self, player: player_entity):
        self.player = player
        self.enemies = [
            Orc_Enemy(orc_race),
            Goblin_Enemy(goblin_race),
            Skeleton_Enemy(skeleton_race)
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
                input(f"round: {turn}, you are have: {self.player.health_points} HP.")
                print("Your Turn.")
                self.player.turn_method(enemy)
                print("Enemy's Turn.")
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
    x = input("what race [H - human, E - Elf, O - Orc]: ").upper()
    race = races[x]
    print(f"{race.name}")

    y = input("what class [B - barbarian, W - wizard]")
    class_ = classes[y]

    player = player_entity(race, class_)
    game = Game(player)
    game.Game_Method()


