class Branch:
    def __init__(self, id: int, name: str, loc: str, ph_n: int, open: bool):
        self.id = id
        self.name = name
        self.location = loc
        self.phone_num = ph_n
        self.open = open

    def __str__(self):
        return f"Branch ID: {self.id} \nBranch Name: {self.name} \nBranch Location: {self.location} \nBranch Phone Number: {self.phone_num} \nBranch Open Status: {self.open}"

    def __repr__(self):
        return f"Branch({self.id}, {self.name}, {self.location}, {self.phone_num}, {self.open})"

    def openBranch(self):
        if not self.open:
            print("already open - unchanged")
        else:
            self.open = True
            print("branch has been opened")
    
    def closeBranch(self):
        if self.open:
            print("already closed - unchanged")
        else:
            self.open = False
            print("branch has been closed")
    
    def updatePhone(self, new_ph: int):
        if new_ph == self.phone_num:
            print("this is already your phone number.")
        else:
            self.phone_num = new_ph
            print(f"your new contact number is: {self.phone_num}")

