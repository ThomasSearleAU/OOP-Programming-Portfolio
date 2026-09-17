# Account class represents a bank account - responsible for managing account details and transactions.
class Account: 
    def __init__(self, id, balance, type):
        if not isinstance(id, int):
            print("invalid data type for id, must be int")
        if not isinstance(balance, (int, float)):
            print("invalid data type for balance, must be float")
        if not isinstance(type, str):
            print("invalid data type for type, must be str")
        else:
            self._id = id
            self._balance = balance
            self.type = type

    # def update_balance(self, adjuster):
    #     self.__balance += adjuster
    #     print(f"new balace: {self.__balance}")
    #     pass
    def deposit(self, amount):
        self._balance += amount
        print(f"balance: {self._balance}")
    
    def withdraw(self, amount):
        self._balance -= amount
        print(f"balance: {self._balance}")

    def get_balance(self):
        print(f"the balance is: {self._balance}")
        return self._balance
    def get_id(self):
        print(f"the id is: {self._id}")
        return self._id
    