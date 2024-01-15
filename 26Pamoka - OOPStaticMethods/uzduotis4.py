class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @staticmethod
    def calculate_payroll(employees):
        return sum(employee.salary for employee in employees)

employees = [Employee("Alice", 5000.0), Employee("Bob", 6000.0), Employee("Charlie", 7000.0)]
print(Employee.calculate_payroll(employees)) # Output: 18000.0