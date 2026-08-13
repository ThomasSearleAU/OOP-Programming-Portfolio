class Account:
    def __init__(self, id, balance, type):
        self.id = id
        self.balance = balance
        self.type = type
    
    def UpdateBalance(self, adjuster):
        self.balance += adjuster
        print(f"new balace: {self.balance}")
        pass

    def getBalance(self):
        print(f"the balance is: {self.balance}")
        return self.balance