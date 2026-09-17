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

class SavingsAccount(Account):

    MIN_BALANCE = 100

    def __init__(self, id, balance, interest_rate):
        super().__init__(id, balance, "Savings Account")
        self.__interest_rate = interest_rate
    
    def withdraw(self, amount):
        if self._balance <= self.MIN_BALANCE:
            print("failed withdrawal: minimum funds for interest already reached")
            return False
        elif self._balance < amount:
            print("failed withdrawal: insufficient funds.")
            return False
        else:
            return super().withdraw(amount)

class EverydayAccount(Account):

    MAX_WITHDRAWAL = 100

    def __init__(self, id, balance):
        super().__init__(id, balance, "Everyday Account")
    
    def withdraw(self, amount):
        if amount > self.MAX_WITHDRAWAL:
            print("failed withdrawal: amount noncompliant with withdrawal specifications for this account.")
            return False
        else:
            return super().withdraw(amount)

    