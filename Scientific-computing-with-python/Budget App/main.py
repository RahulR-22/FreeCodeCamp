class Category:

    def __init__(self, category: str):
        self.category = category
        self.ledger = []
        self._balance = 0

    def deposit(self, amount: float, description: str = ""):
        transaction = {"amount": amount, "description": description}
        self._balance += amount
        self.ledger.append(transaction)

    def withdraw(self, amount: float, description: str = ""):
        if not self.check_funds(amount):
            return False
        transaction = {"amount": -amount, "description": description}
        self._balance -= amount
        self.ledger.append(transaction)
        return True

    def transfer(self, amount: float, categoryObj):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {categoryObj.category}")
        categoryObj.deposit(amount, f"Transfer from {self.category}")
        return True

    def get_balance(self):
        return self._balance

    def check_funds(self, amount: float):
        if self._balance < amount:
            return False
        return True

    def centerDisplay(self, category: str):
        lenCategory = len(category)
        remaining = 30 - lenCategory
        half = remaining // 2
        return f"{'*' * half}{category}{'*' * half}\n"

    def __str__(self):
        response = ""
        response += self.centerDisplay(self.category)
        for transactions in self.ledger:
            response += f"{transactions['description'][:23]:<23}{transactions['amount']:>7.2f}\n"
        response += f"Total: {self._balance}"
        return response


def create_spend_chart(categories):
    pass



