''' 1.
Create a class Animal with a method sound() that prints "Animal makes sound".
Create a class Dog that inherits from Animal and overrides the sound() method to print "Dog barks".
Create an object of Dog and call the sound() method.
'''
# class Animal:
#   def sound(self):
#     print("Animal makes sound")

# class Dog(Animal):
#   def sound(self):
#     print("Dog barks")

# obj = Dog()
# obj.sound()

''' 2.
Create a class Vehicle with a method info() that prints "This is a vehicle".
Create a class Car that inherits from Vehicle and adds a method brand() that prints "Brand is Toyota".
Create an object of Car and call both methods.
'''
# class Vehicle:
#   def info(self):
#     print("This is a vehicle")

# class Car(Vehicle):
#   def brand(self):
#     print("Brand is Toyota")

# obj = Car()
# obj.info()
# obj.brand()

''' 3.
Create a base class Person with __init__ that takes name and age.
Create a derived class Student that inherits from Person and adds roll_number.
Create a Student object and print name, age, and roll_number.
'''
# class Person:
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age

# class Student(Person):
#   def __init__(self,name,age,roll_number):
#     self.name = name
#     self.age = age
#     self.roll_number = roll_number

# obj = Student("Khan Muhammad",19,"133-23-0037")
# print("name: ", obj.name)
# print("age: ",obj.age)
# print("roll number: ",obj.roll_number)

''' 4.
Create a base class Shape with a method area() that just prints "Area not defined".
Create a class Circle that inherits from Shape and overrides area() to calculate and print area using radius.
(Use formula: area = 3.14 * radius * radius)
'''
# class Shape:
#   def area(self):
#     print("Area not defined")

# class Circle(Shape):
#   def __init__(self, radius):
#       self.radius = radius

#   def area(self): 
#       area = 3.14 * self.radius * self.radius
#       print(f"Area is: {area}")

# obj = Circle(5)
# obj.area()

''' 5.
Create a class Employee with a method show_details() that prints name and salary.
Create a class Manager that inherits from Employee and adds a method show_role() that prints "Manager Role".
Create object of Manager and call both methods.
'''
# class Employee:
#    def __init__(self, name, salary):
#        self.name = name
#        self.salary = salary

#    def show_details(self):
#        print("name:", self.name)
#        print("salary:", self.salary)

# class Manager(Employee):
#    def show_role(self):  
#        print("Manager Role")

# obj = Manager("Khan Muhammad", 100000)
# obj.show_details()
# obj.show_role()
