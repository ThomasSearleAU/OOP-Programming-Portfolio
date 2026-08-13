class Client:
    def __init__(self, id, name, mobile_number, email): #constructor
        self.id = id
        self.name = name
        self.mobile_number = mobile_number
        self.email = email
    
    def ChangeContact(self, new_e="", new_m=""):
        print(f"old email: {self.email} \nold phone num: {self.mobile_number}")
        if new_e == "" and new_m == "":
            print("no changes made")
            return
        if new_e != "":
            self.email = new_e
        if new_m != "":
            self.mobile_number = new_m
        print(f"current email: {self.email} \ncurrent phone num: {self.mobile_number}")

    def ChangeName(self, new_name=""):
        if new_name == self.name or new_name=="":
            print("name unchanged: please enter new name")
            return
        else:
            old_name = self.name
            self.name = new_name
            print(f"name changed from {old_name} to {new_name}")
    
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
    
client1 = Client(0, "george", 238472394, "george@george.gg")
client2 = Client(1, "rosemary", 89374983, "mary-rose@the_flower_shop.com")

print(client1.name, client1.id)
print(client2.email, client2.mobile_number)

client1.ChangeContact("george2nd@gmail.com")
client2.ChangeContact("mary-rose@the_flower_shop.com", 123545)

client1.ChangeName()
client2.ChangeName("maryrose")

account1 = Account(0, 50000, "saving")
account2 = Account(1, 32988, "spending")

print(account1.balance, account2.balance)
account1.balance += 20001
account2.balance += 3024
account1.balance -= 20
account2.balance -= 400000000001
print(account1.balance, account2.balance)

print(account1.id)
account2.id = 4   #confirmed changing one obj doesnt change all
print(account1.id)

