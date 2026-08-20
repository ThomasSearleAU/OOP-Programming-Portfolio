class Account:
    def __init__(self, id, balance, type):
        if not isinstance(id, int):
            print("invalid data type for id, must be int")
        if not isinstance(balance, (int, float)):
            print("invalid data type for balance, must be float")
        if not isinstance(type, str):
            print("invalid data type for type, must be str")
        else:
            self.__id = id
            self.__balance = balance
            self.type = type

    # def update_balance(self, adjuster):
    #     self.__balance += adjuster
    #     print(f"new balace: {self.__balance}")
    #     pass
    def deposit(self, amount):
        self.__balance += amount
        print(f"balance: {self.__balance}")
    
    def withdraw(self, amount):
        self.__balance -= amount
        print(f"balance: {self.__balance}")

    def get_balance(self):
        print(f"the balance is: {self.__balance}")
        return self.__balance
    def get_id(self):
        print(f"the id is: {self.__id}")
        return self.__id