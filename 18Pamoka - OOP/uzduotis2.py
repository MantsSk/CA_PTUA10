class Employee:
    def __init__(self, first_name, last_name, company):
        self.first_name = first_name
        self.last_name = last_name
        self.fullname = f"{first_name} {last_name}"
        self.email = f"{first_name.lower()}.{last_name.lower()}@{company.lower()}.com"

employee1 = Employee("John", "Doe", "ExampleCompany")

print("Fullname:", employee1.fullname)
print("Email:", employee1.email)
