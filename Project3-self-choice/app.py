from attacks import *
from dice import *
from entity import *
from race import *


    

    #player = Entity(race, classe, stre, dex, inte, const, wis, char)
x = input("what race [H - human, E - Elf, O - Orc]: ").upper()
race = races[x]
print(f"{race.name}")
