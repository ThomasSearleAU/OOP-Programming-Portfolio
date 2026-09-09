from resource import Resource

class Inventory:
    def __init__(self, inv):
        self.inventory = inv
    
    def add_resource(self, item: Resource):
        if not isinstance(item, Resource):
            print("not correct object type")
            return False
        elif item in self.inventory:
            print('item type already included in inventory')
            return False 
        self.inventory.append(item)
        return True
    

