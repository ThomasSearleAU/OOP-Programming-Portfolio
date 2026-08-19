class Transaction:
    def __init__(self, id: int, type: str, amount: float, desc: str, status: str = "pending"):
        self.__id = id
        self.__type = type
        self.__amount = amount
        self.description = desc
        self.status = status
    def process_transaction(self):
        if self.status == "pending":
            print("processing transaction...")
            self.status = "complete"
            print("transaction processed sucsessfully.")
        elif self.status == "complete":
            print("transaction already satisfied")
        else:
            print("error, transaction failed or denied")
    
    def cancel_transaction(self):
        if self.status == "complete":
            print("transaction already completed, cancellation failed")
        elif self.status == "cancelled":
            print("already cancelled, cancellation failed")
        else:
            print(f"cancelling transaction with id: {self.__id}...")
            self.status = "cancelled"
            print("transaction cancelled")

    def change_desc(self, new_d):
        self.description = new_d
        print(f"description changed to \"{new_d}\"")

    def get_id(self):
        return self.__id
    def get_type(self):
        return self.__type
    def get_amount(self):
        return self.__amount
