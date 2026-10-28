class Race:
    def __init__(self, name, speed, abilities):
        self.name = name
        self.speed = speed
        self.bonuses = {}

elf_race = Race("elf", 30, {"dex":2})
human_race = Race("human", 30, {"str":1, "int":1, "con":1, "dex":1, "wis":1, "cha":1})
orc_race = Race("orc", 15, {"str":2, "con":1, "int":-1})

races = {
    "E": elf_race,
    "H": human_race,
    "O": orc_race
}