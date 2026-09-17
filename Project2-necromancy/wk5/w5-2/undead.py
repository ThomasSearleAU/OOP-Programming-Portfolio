class Undead:
    MAX_HEALTH = 10
    MIN_HEALTH = 1

    MAX_POWER = 10
    MIN_POWER = 1

    MAX_LEVEL = 999

    HEALTH_PER_LEVEL = 2
    POWER_PER_LEVEL = 5

    NAME = "Undead"


    def __init__(self, unit_id, name, type):
        self.__unit_id = unit_id
        self.__name = name
        self.health = self.MIN_HEALTH
        self.power = self.MIN_POWER
        self.__level = 1
        self.type = type

    def get_id(self):
        return self.__unit_id
    
    def level_increase(self):
        self.__level += 1
        if self.health < self.MAX_HEALTH: self.health += self.HEALTH_PER_LEVEL #validates then increases health
        if self.power < self.MAX_POWER: self.power += self.POWER_PER_LEVEL # validates then increases power
    
    def command(self, command):
        print(f"your unit does your bidding, and did: {command}")


    def __str__(self):
        return f"undead number: {self.__unit_id} is {self.__name}, a level {self.__level} undead with {self.health} of {self.MAX_HEALTH} hp and {self.power} of {self.MAX_POWER} power."

#main subclasses

class WarriorUndead(Undead):
    def __init__(self, unit_id, name, type="WarriorUndead"):
        super().__init__(unit_id,name,type)

    def command(self, command):
        print(f"your {self.type} bangs his sheild, and screams an ungodly cry: {command}")

    def combat_style(self):
        print("i fight hard and persistently")

class CursedUndead(Undead):
    def __init__(self, unit_id, name, type="CursedUndead"):
        super().__init__(unit_id,name, type)
    
    def command(self, command):
        print(f"OOOOoooooOOooOOoooo~ your {self.type} moans in a ghoulish manner: {command}") #spoopy O_o
    
    def combat_style(self):
        print("i fight with cursed power and spells")

#"specialised" subclasses

class SkeletonWarrior(WarriorUndead):
    def __init__(self, unit_id, name, hp, power):
        super().__init__(unit_id,name,hp,power, "Skeleton Warrior")

class PhantomGuardian(WarriorUndead):
    def __init__(self, unit_id, name, hp, power):
        super().__init__(unit_id,name,hp,power, "PhantomGuardian")

class VengefulGhost(CursedUndead):
    def __init__(self, unit_id, name, hp, power):
        super().__init__(unit_id,name,hp,power, "VengefulGhost")

class PutridZombie(Undead):
    def __init__(self, unit_id, name, hp, power):
        super().__init__(unit_id,name,hp,power, "PutridZombie")

class DeathKnight(WarriorUndead, CursedUndead):
    MAX_HEALTH = 1000
    MIN_HEALTH = 100
    HEALTH_PER_LEVEL = 100
    POWER_PER_LEVEL = 20
    MIN_POWER = 100
    MAX_POWER = 1000
    NAME = "The Death Knight"
    def __init__(self, unit_id, name, type="DeathKnight"):
        super().__init__(unit_id, name, "DeathKnight")

    def combat_style(self):
        print("i am a death knight! i use the power of killing to chop off heads!")