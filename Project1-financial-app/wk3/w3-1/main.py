from modules.clients import Client
from modules.accounts import Account
from modules.transactions import Transaction
from modules.branches import Branch
client1 = Client(0, "george", 238472394, "george@george.gg")
client2 = Client(1, "rosemary", 89374983, "mary-rose@the_flower_shop.com")

print(client1.name, client1.get_id())
print(client2.get_email(), client2.get_mobile())

client1.change_contact("george2nd@gmail.com")
client2.change_contact("mary-rose@the_flower_shop.com", 123545)

client1.change_name()
client2.change_name("maryrose")

account1 = Account(0, 50000, "saving")
account2 = Account(1, 32988, "spending")

print(account1.get_balance(), account2.get_balance())
account1.deposit(20001)
account2.deposit(3024)
account1.withdraw(20)
account2.withdraw(400000000001)
print(account1.get_balance(), account2.get_balance())

print(account1.get_id())
account2.id = 4   #confirmed changing one obj doesnt change all
print(account1.get_id())

Transaction1 = Transaction(0, "transfer", 4, "fungile business", "pending")
Transaction1.cancel_transaction()
Transaction1.cancel_transaction()
Transaction1.process_transaction()

Branch1 = Branch(0, "branch1", "location1", 123456789, True)
Branch1.close_branch()



print(f"{repr(Branch1)} print one") #why does this print the memory address instead of the string representation?
print(f"{str(Branch1)} print two") 


print(str(Branch1)+" print three")
print(Branch1) #this prints the string representation as expected
repr(Branch1)
print(Branch1)#this prints the string representation as expected

str(Transaction1)
print(Transaction1) #this prints the string representation as expected
print(str(Transaction1))



