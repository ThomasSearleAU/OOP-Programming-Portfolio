class Client:
    def __init__(self, id, name, mobile_number, email): #constructor
        self.__id = id
        self.name = name
        self.__mobile_number = mobile_number
        self.__email = email
    
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
