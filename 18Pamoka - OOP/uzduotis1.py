class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error: Division by zero"
        else:
            return x / y

calculator = Calculator()

result_addition = calculator.add(5, 3)
result_subtraction = calculator.subtract(8, 4)
result_multiplication = calculator.multiply(2, 6)
result_division = calculator.divide(10, 2)

print("Addition: ", result_addition)
print("Subtraction: ", result_subtraction)
print("Multiplication: ", result_multiplication)
print("Division: ", result_division)
