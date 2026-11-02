# inheritance
class Employee:
    def __init__(self, name, email, department,salary):
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary
    def show_details(self):
        print(self.name, self.email, self.department, self.salary)

class PermanentEmployee(Employee): # inheriting
    def __init__(self, name, email, department, salary, cover, increment):
       super().__init__(name,email,department,salary)
       self.cover = cover
       self.increment = increment

class ContractEmployee(Employee):
    def __init__(self, name, email, department, salary, tenure):
        super().__init__(name, email, department, salary)
        self.tenure = tenure
    def show_details(self):
        print(f"name{self.name}")
        print(f"email{self.email}")
        print(f"contract length{self.tenure}")

# dbr


p1 = PermanentEmployee('Suheila Mohamed', 'suheila@gmail.com', 'Legal', 100_000,'Britam', 5000)
c1 = ContractEmployee('Kambe Kiwana', 'kiwana@gmail.com','HR',88_000,3)

p1.show_details()
c1.show_details()

# TODO overriding
# oop in python
