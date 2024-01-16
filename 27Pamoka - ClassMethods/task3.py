class BankAccount:
    total_accounts = 0

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1

    def show_balance(self):
        print(f"{self.owner}'s account balance: ${self.balance}")

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

    @staticmethod
    def validate_amount(amount):
        return amount > 0

# Creating instances
account1 = BankAccount("Alice", 1000.0)
account2 = BankAccount("Bob", 500.0)

# Using instance method
account1.show_balance()
account2.show_balance()

# Using class method
print("Total Bank Accounts:", BankAccount.get_total_accounts())

# Using static method
print("Is 200 a valid amount?", BankAccount.validate_amount(200))
print("Is -50 a valid amount?", BankAccount.validate_amount(-50))
