class BankAccount:
    def __init__(self):
        self._balance = 0 

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance

# Example usage:
account = BankAccount()
account.deposit(1000)
account.withdraw(500)
print(account.get_balance())  # Output: 500
