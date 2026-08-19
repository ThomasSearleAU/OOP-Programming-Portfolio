class Branch:
    def __init__(self, id: int, name: str, loc: str, ph_n: int, open: bool):
        self.__id = id
        self.name = name
        self.location = loc
        self.__phone_num = ph_n
        self.__open = open
    def open_branch(self):
        if self.__open == False:
            print("already open - unchanged")
        else:
            self.__open = True
            print("branch has been opened")
    
    def close_branch(self):
        if self.__open == True:
            print("already closed - unchanged")
        else:
            self.__open = False
            print("branch has been closed")
    
    def update_phone(self, new_ph: int):
        if new_ph == self.__phone_num:
            print("this is already your phone number.")
        else:
            self.__phone_num = new_ph
            print(f"your new contact number is: {self.__phone_num}")
    def get_id(self):
        return self.__id

