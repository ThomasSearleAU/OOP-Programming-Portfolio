class Transaction:
    def __init__(self, id: int, type: str, amount: float, desc: str, status: str = "pending"):
        self.id = id
        self.type = type
        self.amount = amount
        self.description = desc
        self.status = status

    def __str__(self):
        return f"Transaction id: {self.id} \nTransaction type: {self.type} \nTransaction amount: {self.amount} \ntransaction Type: {self.type} \nTransaction Status: {self.status}"

    def __repr__(self):
        return f"Transaction({self.id}, {self.type}, {self.amount}, {self.description}, {self.status})"

    def processTransaction(self):
        if self.status == "pending":
            print("processing transaction...")
            self.status = "complete"
            print("transaction processed sucsessfully.")
        elif self.status == "complete":
            print("transaction already satisfied")
        else:
            print("error, transaction failed or denied")
    
    def cancelTransaction(self):
        if self.status == "complete":
            print("transaction already completed, cancellation failed")
        elif self.status == "cancelled":
            print("already cancelled, cancellation failed")
        else:
            print(f"cancelling transaction with id: {self.id}...")
            self.status = "cancelled"
            print("transaction cancelled")

    def changeDesc(self, new_d):
        self.description = new_d
        print(f"description changed to \"{new_d}\"")
