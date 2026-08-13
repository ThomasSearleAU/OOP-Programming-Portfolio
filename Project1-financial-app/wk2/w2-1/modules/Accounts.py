class Account:
    def __init__(self, id, balance, type):
        self.id = id
        self.balance = balance
        self.type = type
    
    def __str__(self):
        return f"Account ID: {self.id} \nAccount Balance: {self.balance} \nAccount Type: {self.type}"
    
    def __repr__(self):
        return f"Account({self.id}, {self.balance}, {self.type})"

    def UpdateBalance(self, adjuster):
        self.balance += adjuster
        print(f"new balace: {self.balance}")
        pass

    def getBalance(self):
        print(f"the balance is: {self.balance}")
        return self.balance