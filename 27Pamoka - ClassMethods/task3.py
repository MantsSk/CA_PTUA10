class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds")
        else:
            self.balance -= amount

    @classmethod
    def from_balance(cls, balance):
        return cls(balance)

    @staticmethod
    def transfer(from_account, to_account, amount):
        if from_account.balance < amount:
            print("Insufficient funds in the source account")
        else:
            from_account.withdraw(amount)
            to_account.deposit(amount)

# Create a new bank account with a balance of 100
account1 = BankAccount.from_balance(100)

# Create a new bank account with a balance of 50
account2 = BankAccount.from_balance(50)

# Transfer 20 from account1 to account2
BankAccount.transfer(account1, account2, 20)

# Print the balances
print(account1.balance)  # Should print 80
print(account2.balance)  # Should print 70
