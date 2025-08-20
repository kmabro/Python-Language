'''
Create a class `Animal` with a method `speak()` that prints "Animal speaks".
Create a class `Dog` that inherits from `Animal`.
In the Dog class, override the `speak()` method to print "Dog barks"
Also use `super()` inside the Dog's `speak()` to call the parent method.
Then create an object of Dog and call its speak method.
'''
# class Animal:
#   def speak(self):
#     print("Animal speaks")

# class Dog(Animal):
#   def speak(self):
#     super().speak()
#     print("Dog barks")

# dog = Dog()
# dog.speak()

'''
Create a class `Person` with __init__ method that accepts name and prints "Person: name"
Create a class `Student` that inherits from `Person`
In `Student`, use `super().__init__(name)` inside its constructor and also print "Student created"
Create a `Student` object with name and observe the output
'''
# class Person:
#   def __init__(self, name):
#     self.name = name
#     print(f"Person: {self.name}")

# class Student(Person):
#   def __init__(self, name):
#     super().__init__(name)
#     print("Student created")

# st = Student("John")
# print(st.name)

'''
Create class `ClassA` with method show() that prints "This is ClassA"
Create class `ClassB` with method show() that prints "This is ClassB"
Create class `Derived` that inherits from ClassA and ClassB
In Derived class, override `show()` method and use `super().show()`
Create object of Derived and call show()
Observe which class's method is called due to method resolution order
'''
# class ClassA:
#   def show(self):
#     print("This is ClassA")

# class ClassB:
#   def show(self):
#     print("This is ClassB")

# class Derived(ClassA, ClassB):
#   def show(self):
#     super().show()
#     print("This is Derived")

# obj = Derived()
# obj.show()

'''
Create three classes: A, B, and C
A has a method greet() that prints "Hello from A"
B inherits from A and overrides greet(), calling `super().greet()` and then printing "Hello from B"
C inherits from B and overrides greet(), calling `super().greet()` and then printing "Hello from C"
Create an object of C and call greet()
Observe how super() works in multi-level inheritance
'''
# class A:
#   def greet(self):
#       print("Hello from A")

# class B(A):  
#   def greet(self):
#       super().greet()  
#       print("Hello from B")

# class C(B):  
#   def greet(self):
#       super().greet() 
#       print("Hello from C")

# c = C()
# c.greet()  

'''
Create a class Person with attributes name and age.
Create a subclass Student that inherits from Person and adds a new attribute grade.
Use super() to initialize the parent class attributes.
Create an object of Student and print name, age, and grade.
'''
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# class Student(Person):
#   def __init__(self, name, age, grade):
#     super().__init__(name, age)
#     self.grade = grade

# obj = Student("km_abro", 19, "A")
# print(obj.name, obj.age, obj.grade)

'''
Create a class Device with an attribute brand.
Create a subclass Phone that adds an attribute model.
Use super() to call the parent constructor.
Create a Phone object and print brand and model.
'''
# class Device:
#   def __init__(self, brand):
#     self.brand = brand

# class Phone(Device):
#   def __init__(self, brand, model):
#     super().__init__(brand)
#     self.model = model

# phone = Phone("Apple", "iPhone 13")
# print(phone.brand, phone.model)

'''
Create a base class Shape with an attribute color.
Create a subclass Circle that adds radius.
Use super() to set the color in Shape.
Create a Circle object and print color and radius.
'''
# class Shape:
#   def __init__(self, color):
#     self.color = color

# class Circle(Shape):
#   def __init__(self, color, radius):
#     super().__init__(color)
#     self.radius = radius

# obj = Circle("red", 5)
# print(obj.color, obj.radius)

'''
Create a class Account with owner and balance attributes.
Create a subclass SavingsAccount that adds interest_rate.
Use super() to initialize the base class.
Create an object of SavingsAccount and print all its attributes.
'''
# class Amount:
#   def __init__(self, owner, balance):
#     self.owner = owner
#     self.balance = balance

# class SavingsAccount(Amount):
#   def __init__(self, owner, balance, interest_rate):
#     super().__init__(owner, balance)
#     self.interest_rate = interest_rate

# obj = SavingsAccount("km_abro", 1000, 0.05)
# print(obj.owner, obj.balance, obj.interest_rate)