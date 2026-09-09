class Resource:
    def __init__(self, quantity):
        self.id
        self.name
        self.type
        self.__quantity = quantity

    def __get_quantity(self):
        return self.__quantity
    
    def __set_quantity(self, setter):
        self.__quantity = setter
    quantity = property(__get_quantity, __set_quantity)
