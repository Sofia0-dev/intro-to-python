#oop2

class Circle:
    def __init__(self, radius): # setup
        self.radius = radius

    def area(self):
        return 22/7 * self.radius**2

    def perimeter(self):
        return 2 * self.radius* 2

    def print_details(self):
        print("Radius is", self.radius)
        print("Perimeter is", self.perimeter())
        print("Area is", self.area())

c1 = Circle(10)
c2 = Circle(28)
c3 = Circle(40)


print(c1.area())
c1.print_details()


# branches -- copy -- master main
# feature ---

# we will learn inheritance in python