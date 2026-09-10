from resource import Resource
ALL_ITEMS = [
    Resource(0, "Necrotic Rune", 0),
    Resource(1, "Spirit Rune", 0),
    Resource(2, "Bone Rune", 0),
    Resource(3, "Flesh Rune", 0),
    Resource(4, "Ectoplasm", 0)
]
class Inventory:
    def __init__(self):
        self.inventory = ALL_ITEMS

    def add_resource(self, item: Resource):
        if not isinstance(item, Resource):
            print("not correct object type")
            return False
        elif item in self.inventory:
            print('item type already included in inventory')
            return False 
        self.inventory.append(item)
        return True
    
    def check_requirements(self, ritual):
        for item in self.inventory:
            if item.quantity < ritual.get(item.name, 0):
                return False
        return True
    def spend_ritual_cost(self, ritual):
        if self.check_requirements(ritual):
            for item in self.inventory:
                item.change_quantity(-ritual.get(item.name, 0))