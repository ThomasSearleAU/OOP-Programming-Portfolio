from modules.accounts import Account
from modules.branches import Branch
# Client class represents a bank client - responsible for managing client details and accounts.
class Client:
    def __init__(self, id, name, mobile_number, email): #constructor
        if not isinstance(id, int):
            print("invalid data type for id, must be int")
        if not isinstance(name, str):
            print("invalid data type for name, must be str")
        if not isinstance(mobile_number, str):
            print("invalid data type for mobile_number, must be str")
        if not isinstance(email, str):
            print("invalid data type for email, must be str")
        else:
            self.__id = id
            self.name = name
            self.__mobile_number = mobile_number
            self.__email = email
            self.accounts = []
            self.preferred_branch = None

    def set_preferred_branch(self, branch: Branch):
        if not isinstance(branch, Branch):
            print("invalid data type for branch, must be Branch")
            return
        self.preferred_branch = branch
        print(f"preferred branch for client {self.name} set to {branch.name}")

    def add_account(self, account: Account):
        if not isinstance(account, Account):
            print("invalid data type for account, must be Account")
            return
        elif account in self.accounts:
            print(f"account with id {account.get_id()} already exists for client {self.name}")
            return
        self.accounts.append(account)
        print(f"account with id {account.get_id()} added to client {self.name}")

    def remove_account(self, account: Account):
        if not isinstance(account, Account):
            print("invalid data type for account, must be Account")
            return
        elif account not in self.accounts:
            print(f"account with id {account.get_id()} does not exist for client {self.name}")
            return
        self.accounts.remove(account)
        print(f"account with id {account.get_id()} removed from client {self.name}")
    
    def __str__(self):
        return f"Client ID: {self.__id} \nClient Name: {self.name} \nClient Mobile Number: {self.__mobile_number} \nClient Email: {self.__email}"

    def __repr__(self):
        return f"Client({self.__id}, {self.name}, {self.__mobile_number}, {self.__email})"

    def change_contact(self, new_e="", new_m=""):
        print(f"old email: {self.__email} \nold phone num: {self.__mobile_number}")
        if new_e == "" and new_m == "":
            print("no changes made")
            return
        if new_e != "":
            self.__email = new_e
        if new_m != "":
            self.__mobile_number = new_m
        print(f"current email: {self.__email} \ncurrent phone num: {self.__mobile_number}")

    def change_name(self, new_name=""):
        if new_name == self.name or new_name=="":
            print("name unchanged: please enter new name")
            return
        else:
            old_name = self.name
            self.name = new_name
            print(f"name changed from {old_name} to {new_name}")
    
    def get_id(self):
        return self.__id
    
    def get_email(self):
        return self.__email
    def get_mobile(self):
        self.__mobile_number
