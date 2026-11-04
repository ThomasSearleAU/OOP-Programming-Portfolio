import random

from attacks import *
from dice import *
from entity import *
from race import *


enemies = [
    Orc_Enemy(orc_race),
    Goblin_Enemy(goblin_race),
    Skeleton_Enemy(skeleton_race)
]   

    #player = Entity(race, classe, stre, dex, inte, const, wis, char)
x = input("what race [H - human, E - Elf, O - Orc]: ").upper()
race = races[x]
print(f"{race.name}")


def Game(player: player_entity):
    while player.health_points > 0:
        enemy = random.choice(enemies)

