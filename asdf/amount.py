from datetime import datetime

class Amount:
    def __init__(self, amount: float, transaction_type: str):
        self.amount = amount
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type

    def __str__(self):
        return f"[{self.timestamp}] {self.transaction_type}: ${self.amount:.2f}"
