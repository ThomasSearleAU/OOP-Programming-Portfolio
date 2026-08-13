class Client:
    def __init__(self, id, name, mobile_number, email): #constructor
        self.id = id
        self.name = name
        self.mobile_number = mobile_number
        self.email = email
    
    def __str__(self):
        return f"Client ID: {self.id} \nClient Name: {self.name} \nClient Mobile Number: {self.mobile_number} \nClient Email: {self.email}"

    def __repr__(self):
        return f"Client({self.id}, {self.name}, {self.mobile_number}, {self.email})"

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
