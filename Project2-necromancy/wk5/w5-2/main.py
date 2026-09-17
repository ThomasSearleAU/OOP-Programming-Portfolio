from resource import *
from inventory import *
from undead import * 
from necromancer import * 
from resource import *

necromancer = Necromancer("Bobby", "Necromancer")
inventory = Inventory(necromancer)

DeathKnightRitual = Ritual(DeathKnight, "deathKnight", "DeathKnightRitual", 99,99,99,99,99)

DeathKnightRitual.summon_undead(inventory)




