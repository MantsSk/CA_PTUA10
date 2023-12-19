class CoffeeMachine:
    def __init__(self):
        self.water_level = 100  # Initial water level
        self.coffee_beans_level = 50  # Initial coffee beans level
        self.milk_level = 30  # Initial milk level

    def brew_espresso(self):
        if self.water_level >= 30 and self.coffee_beans_level >= 15:
            print("Brewing Espresso...")
            self.water_level -= 30
            self.coffee_beans_level -= 15
            print("Espresso is ready!")
        else:
            print("Insufficient resources to brew Espresso. Please refill.")

    def brew_latte(self):
        if self.water_level >= 30 and self.coffee_beans_level >= 15 and self.milk_level >= 10:
            print("Brewing Latte...")
            self.water_level -= 30
            self.coffee_beans_level -= 15
            self.milk_level -= 10
            print("Latte is ready!")
        else:
            print("Insufficient resources to brew Latte. Please refill.")

    def refill_water(self, amount):
        self.water_level += amount
        print(f"Water refilled by {amount} units.")

    def refill_coffee_beans(self, amount):
        self.coffee_beans_level += amount
        print(f"Coffee beans refilled by {amount} units.")

    def refill_milk(self, amount):
        self.milk_level += amount
        print(f"Milk refilled by {amount} units.")

    def display_status(self):
        print(f"\nCurrent Water Level: {self.water_level} units")
        print(f"Current Coffee Beans Level: {self.coffee_beans_level} units")
        print(f"Current Milk Level: {self.milk_level} units")


coffee_machine = CoffeeMachine()

while True:
    print("\nActions:")
    print("1. Brew Espresso")
    print("2. Brew Latte")
    print("3. Refill Water")
    print("4. Refill Coffee Beans")
    print("5. Refill Milk")
    print("6. Display Status")
    print("0. Exit")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        coffee_machine.brew_espresso()
    elif choice == "2":
        coffee_machine.brew_latte()
    elif choice == "3":
        amount = int(input("Enter the amount to refill water: "))
        coffee_machine.refill_water(amount)
    elif choice == "4":
        amount = int(input("Enter the amount to refill coffee beans: "))
        coffee_machine.refill_coffee_beans(amount)
    elif choice == "5":
        amount = int(input("Enter the amount to refill milk: "))
        coffee_machine.refill_milk(amount)
    elif choice == "6":
        coffee_machine.display_status()
    elif choice == "0":
        print("Exiting the Coffee Machine. Have a great day!")
        break
    else:
        print("Invalid choice. Please enter a valid number.")
