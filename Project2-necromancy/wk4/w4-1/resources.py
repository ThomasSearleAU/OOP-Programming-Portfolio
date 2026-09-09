class Resource:
    def __init__(self, quantity):
        self.id
        self.name
        self.type
        self.__quantity = quantity
    @property
    def get_quantity(self):
        return self.__quantity
    
    def set_quantity(self):
        if self.__quantity:
            pass