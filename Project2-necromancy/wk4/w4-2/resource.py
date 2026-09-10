class Resource:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.__quantity = quantity

    def __get_quantity(self):
        return self.__quantity
    
    def __set_quantity(self, setter):
        self.__quantity = setter

    def change_quantity(self, edit):
        self.__quantity += edit
    quantity = property(__get_quantity, __set_quantity, change_quantity)
