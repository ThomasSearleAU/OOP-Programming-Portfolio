from modules.clients import Client
from modules.accounts import Account
from modules.transactions import Transaction
from modules.branches import Branch

client1 = Client(1, "John Doe", 1234567890, "john.doe@example.com")
client2 = Client(2, "Jane Smith", 9876543210, "jane.smith@example.com")
client3 = Client(3, "Alice Johnson", 5555555555, "alice.johnson@example.com")

account1 = Account(1, 1000.0, "savings")
account2 = Account(2, 500.0, "checking")    
account3 = Account(3, 2000.0, "savings")

branch1 = Branch(1, "Main Branch", "123 Main St", 1234567890, True)
branch2 = Branch(2, "Second Branch", "456 Second St", 9876543210, False)
branch3 = Branch(3, "Third Branch", "789 Third St", 5555555555, True)

transaction1 = Transaction(1, "deposit", 100.0, "Deposit to savings account", "pending")
transaction2 = Transaction(2, "withdrawal", 50.0, "Withdrawal from checking account", "completed")
transaction3 = Transaction(3, "transfer", 200.0, "Transfer from savings to checking", "pending")


print(client1.get_email())
print(client2.get_id())
print(client3.get_mobile())

example_client = Client(4, "Bob Brown", 1112223333, "bob.brown@example.com")
example_fail = Client("invalid_id", "Invalid User", 1234567890, "invalid.email@example.com")   

client1.add_account(account1)
client1.add_account(account1)  # Attempt to add the same account again

client2.add_account(account2)
client3.add_account(account3)
client2.remove_account(account2)
print(account2)

client1.set_preferred_branch(branch1)