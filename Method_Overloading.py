'''
Create a class `Animal` with a method `sound()` that prints "Some generic sound".
Create a class `Dog` that inherits from `Animal` and overrides the `sound()` method to print "Bark".
Create an object of `Dog` and call the `sound()` method.
'''
# class Animal:
#   def sound(self):
#     print("Some generic sound")

# class Dog(Animal):
#   def sound(self):
#     print("Bark")

# obj = Dog()
# obj.sound()

'''
Create a base class `Vehicle` with a method `start()` that prints "Starting vehicle...".
Create a derived class `Car` that overrides the `start()` method to print "Car engine started".
Call the method using an object of `Car`.
'''
# class Vehicle:
#   def start(self):
#     print("Starting vehicle...")

# class Car(Vehicle):
#   def start(self):
#     print("Car engine started")

# obj = Car()
# obj.start()

'''
Create a class `Employee` with a method `get_role()` that prints "Employee".
Create a class `Manager` that inherits from `Employee` and overrides the `get_role()` method to print "Manager".
Create a class `Developer` that also inherits from `Employee` and overrides `get_role()` to print "Developer".
Test both subclasses.
'''
# class Employee:
#   def get_role(self):
#     print("Employee")

# class Manager(Employee):
#   def get_role(self):
#     print("Manager")

# class Developer(Employee):
#   def get_role(self):
#     print("Developer")

# obj1 = Manager()
# obj1.get_role()
# obj2 = Developer()
# obj2.get_role()

'''
Create a base class `Printer` with a method `print_message()` that prints "Base print".
Create a class `ColorPrinter` that overrides `print_message()` to print "Color print", but also calls the base class method using `super()`.
Test the overridden method.
'''
# class Printer:
#   def print_message(self):
#     print("Base print")

# class ColorPrinter(Printer):
#   def print_message(self):
#     super().print_message()
#     print("Color print")

# obj = ColorPrinter()
# obj.print_message()

'''
Create a base class `Shape` with a method `area()` that prints "Calculating area...".
Create a class `Rectangle` with attributes `width` and `height` that overrides the `area()` method.
It should call `super().area()` and then return the area of the rectangle.
'''
# class Shape:
#   def area(self):
#     print("Calculating area...")

# class Rectangle(Shape):
#   def __init__(self, width, height):
#     self.width = width
#     self.height = height
#     super().area()
#     print(self.width * self.height)

# obj = Rectangle(5, 10)

'''
Create a class `Shape` with a method `area()` that returns 0.
Create a subclass `Circle` with an attribute `radius` that overrides `area()` and returns the area of the circle (π * r^2).
Create a subclass `Square` with attribute `side` that overrides `area()` and returns the area of the square (side * side).
Create objects of both and print their areas.
'''
# class Shape:
#   def area(self):
#     return 0

# class Circle(Shape):
#   def __init__(self, radius):
#     self.radius = radius

#   def area(self):
#     return 3.14 * self.radius ** 2

# class Square(Shape):
#   def __init__(self, side):
#     self.side = side

#   def area(self):
#     return self.side * self.side

# circle = Circle(5)
# print(circle.area())

# square = Square(5)
# print(square.area())

'''
Create a base class `Account` with attributes `balance`, and a method `calculate_interest()` that returns balance * 0.01.
Create a subclass `SavingsAccount` that overrides `calculate_interest()` to return balance * 0.04.
Create a subclass `CurrentAccount` that overrides `calculate_interest()` to return balance * 0.02.
Create objects of each and print their interest.
'''
# class Amount:
#   def __init__(self, balance):
#     self.balance = balance

#   def calculate_interest(self):
#     return self.balance * 0.01

# class SavingsAccount(Amount):
#   def calculate_interest(self):
#     return self.balance * 0.04

# class CurrentAccount(Amount):
#   def calculate_interest(self):
#     return self.balance * 0.02

# obj1 = SavingsAccount(1000)
# print(obj1.calculate_interest())

# obj2 = CurrentAccount(1000)
# print(obj2.calculate_interest())

'''
Create a class `Employee` with attributes `name` and `base_salary`, and a method `calculate_salary()` that returns the base salary.
Create a subclass `Manager` that overrides `calculate_salary()` to return base salary + 5000 bonus.
Create a subclass `Developer` that overrides it to return base salary + 3000 bonus.
Create objects of each and print their salaries.
'''
# class Employee:
#   def __init__(self, name, base_salary):
#     self.name = name
#     self.base_salary = base_salary

#   def calculate_salary(self):
#     return self.base_salary

# class Manager(Employee):
#   def calculate_salary(self):
#     return self.base_salary + 5000

# class Developer(Employee):
#   def calculate_salary(self):
#     return self.base_salary + 3000

# obj1 = Manager("abc", 50000)
# print(obj1.calculate_salary())
# obj2 = Developer("xyz", 50000)
# print(obj2.calculate_salary())