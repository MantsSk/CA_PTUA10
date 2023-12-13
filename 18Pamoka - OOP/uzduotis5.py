class Record:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount

    def __str__(self):
        return f"{self.type}: {self.amount}"


class Budget:
    def __init__(self):
        self.journal = []

    def add_income_record(self, amount):
        income_record = Record("Income", amount)
        self.journal.append(income_record)

    def add_expense_record(self, amount):
        expense_record = Record("Expense", amount)
        self.journal.append(expense_record)

    def get_balance(self):
        total = 0
        for record in self.journal:
            if record.type == "Income":
                total += record.amount
            if record.type == "Expense":
                total -= record.amount
        print(total)

    def show_report(self):
        for record in self.journal:
            print(f"{record.type}: {record.amount}")


budget = Budget()

while True:
    choice = int(input("1 - enter income, \n2 - enter expense, \n3 - get balance, \n4 - show report, \n9 - exit the program"))
    if choice == 1:
        amount = float(input("Enter the income amount: "))
        budget.add_income_record(amount)
    if choice == 2:
        amount = float(input("Enter the expense amount: "))
        budget.add_expense_record(amount)
    if choice == 3:
        budget.get_balance()
    if choice == 4:
        budget.show_report()
    if choice == 9:
        print("Goodbye")
        break
