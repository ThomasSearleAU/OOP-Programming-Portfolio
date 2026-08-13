from modules.Clients import Client
from modules.Accounts import Account
from modules.Transactions import Transaction
from modules.Branches import Branch
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

Transaction1 = Transaction(0, "transfer", 4, "fungile business", "pending")
Transaction1.cancelTransaction()
Transaction1.cancelTransaction()
Transaction1.processTransaction()

Branch1 = Branch(0, "branch1", "location1", 123456789, True)
Branch1.closeBranch()


print(repr(Branch1)) #why does this print the memory address instead of the string representation?
print(str(Branch1)) #this prints the string representation as expected