import random

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

Dcoin = Dice(2)    
D4 = Dice(4)
D6 = Dice(6)
D8 = Dice(8)
D10 = Dice(10)
D12 = Dice(12)
D20 = Dice(20)
Dchance = Dice(100)