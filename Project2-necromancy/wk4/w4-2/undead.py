class Undead:
    MAX_HEALTH = 10
    MIN_HEALTH = 1

    MAX_POWER = 10
    MIN_POWER = 1

    MAX_LEVEL = 999

    HEALTH_PER_LEVEL = 2
    POWER_PER_LEVEL = 5


    def __init__(self, unit_id, name, hp, power, type):
        self.__unit_id = unit_id
        self.__name = name
        self.__health = hp
        self.__power = power
        self.__level = 1
        self.type

    def get_id(self):
        return self.__unit_id
    
    def level_increase(self):
        self.__level += 1
        if self.__health < self.MAX_HEALTH: self.__health += self.HEALTH_PER_LEVEL #validates then increases health
        if self.__power < self.MAX_POWER: self.__power += self.POWER_PER_LEVEL # validates then increases power

    def __str__(self):
        return f"undead number: {self.__unit_id} is {self.__name}, a level {self.__level} undead with {self.__health} of {self.MAX_HEALTH} hp and {self.__power} of {self.MAX_POWER} power."

