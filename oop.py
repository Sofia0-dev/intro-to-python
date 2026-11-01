#oop
#object --> laptop --> Mac
# name --> properties
#classes

class Person:
    # constructor
    def __init__(self, name, dob, color, weight, height,age):
        self.name = name
        self.age = age
        self.dob = dob
        self.color = color
        self.weight = weight
        self.height = height
    def display(self):
        print(f"Name is {self.name} and age is {self.age}")

    def get_bmi(self):
        result = self.weight/ self.height**2
        return result(result,2)



# blueprint for creating objects

p1 = Person("Sofie","07-26-2001", "Black", 55, 168)
p2 = Person("Suheila", "12-17-2014", "White", 25, 143)

p1.display()
p2.display()

print(p1.get_bmi())

print(f"{p1.name}  bmi is {p1.get_bmi()}")
print(f"{p2.name}  bmi is {p2.get_bmi()}")
