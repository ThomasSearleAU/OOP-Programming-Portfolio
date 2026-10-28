from attacks import *
from dice import *
from entity import *

def player_init():
    race = input("what race [H - human, E - Elf, O - Orc]: ").upper

    player = Entity(race, classe, stre, dex, inte, const, wis, char)
