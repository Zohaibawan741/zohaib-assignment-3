class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"Deposited ${amount}. Current balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew ${amount}")
                return f"Withdrew ${amount}. Current balance: ${self.balance}"
            else:
                return "Insufficient funds."
        else:
            return "Invalid withdrawal amount."

    def balance_inquiry(self):
        return f"Current balance: ${self.balance}"

    def get_transaction_history(self):
        return self.transaction_history

account = BankAccount()

print(account.deposit(100))
print(account.withdraw(30))
print(account.balance_inquiry())
print(account.get_transaction_history())