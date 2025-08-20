''' 1.
Create a class `MyClass` with a class variable `message = "Hello"`.
Add a class method `print_message(cls)` that prints the value of `message`.
Call the method using the class.
'''
# class MyClass:
#   message = "Hello"

#   @classmethod
#   def print_message(cls):
#     print(cls.message)

# MyClass.print_message()
''' 2.
Create a class `School` with a class variable `school_name = "ABC High School"`.
Add a class method `change_school_name(cls, new_name)` that updates the school name.
Call the method to change the name, then print the updated name.
'''
# class School:
#   school_name = "ABC High School"

#   @classmethod
#   def chnage_school_name(cls, new_name):
#     cls.school_name = new_name
#     print(f"New school name is {cls.school_name}")

# s1 = School()
# s1.chnage_school_name("XYZ High School")
''' 3.
Create a class `Counter` with:
- class variable `count = 0`
- constructor that increases `count` by 1 whenever an object is created
- class method `show_count(cls)` to print how many objects were created
Create 2 objects and call `show_count()`.
'''
# class Counter:
#   count = 0
#   def __init__(self):
#     Counter.count += 1
#     print(f"Object number {Counter.count} created")

#   @classmethod
#   def show_count(cls):
#     print(f"Total objects created are {cls.count}")

# c1 = Counter()
# c2 = Counter()
# c2.show_count()
''' 4.
Create a class `Student` with `name` and `age`.
Add a class method `from_string(cls, data)` that takes a string like "Ali,20"
and returns a Student object.
Use the class method to create a student and print their details.
'''
# class Student:
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age

#   @classmethod
#   def from_string(cls, data):
#     name, age = data.split(",")
#     return cls(name, age)

# st1 = Student.from_string("Ali,20")
# print(st1.name, st1.age)
''' 5.
Create a class `Rectangle` with `length` and `width`.
Add a class method `create_square(cls, side)` that returns a Rectangle with equal sides.
Create a square using the class method and print its sides.
'''
# class Rectangle:
#   def __init__(self, length, width):
#     self.length = length
#     self.width = width

#   @classmethod
#   def create_square(cls, side):
#     return cls(side, side)

# sq1 = Rectangle.create_square(5)
# print(sq1.length, sq1.width)
''' 6.
Create a class `Book` with a class variable `category = "Literature"`.
Add a class method `change_category(cls, new_category)` to change the value of the class variable.
Call the method and print the new category.
'''
# class Book:
#   category = "Literature"

#   @classmethod
#   def change_category(cls, new_category):
#     cls.category = new_category
#     print(f"New category is {cls.category}")

# b1 = Book()
# b1.change_category("Science")
''' 7.
Create a class `Employee` that has:
- a class variable `employee_count` initialized to 0
- in the __init__, increment `employee_count`
- a class method `total_employees(cls)` that prints the total number of employees created
Create 3 Employee objects and use the class method to print the count.
'''
# class Employee:
#   employee_count = 0
#   def __init__(self):
#     Employee.employee_count += 1
#     print(f"Employee number {Employee.employee_count} created")

#   @classmethod
#   def total_employees(cls):
#     print(f"Total employees are {cls.employee_count}")

# e1 = Employee()
# e2 = Employee()
# e2.total_employees()
# e3 = Employee()
# e3.total_employees()



##### Class Methods as Alternative Constructors #####


''' 1.
Create a class `Person` with attributes: name and age
Write a class method `from_string(cls, data)` that takes a string like "Ali,22"
and returns a Person object.
Create a person using the class method and print their name and age.
'''
# class Person:
#   def __init__(self, name, age):
#     self.name  = name
#     self.age = age

#   @classmethod
#   def from_string(cls,data):
#     name, age = data.split(",")
#     return cls(name, age)

# p1 = Person.from_string("Ali,22")
# print(p1.name, p1.age)

''' 2.
Create a class `Student` with attributes: name and grade
Write a class method `from_dict(cls, data)` where `data` is a dictionary like:
{"name": "KM", "grade": "A"}
Return a Student object from this dictionary.
'''
# class Student:
#   def __init__(self, name, grade):
#     self.name = name
#     self.grade = grade

#   @classmethod
#   def from_dict(cls,data):
#     return cls(data["name"], data["grade"])

# st1 = Student.from_dict({"name": "KM", "grade": "A"})
# print(st1.name, st1.grade)

''' 3.
Create a class `Rectangle` with width and height
Add a class method `square(cls, side)` that returns a square (width = height = side)
Create a square and print its width and height.
'''
# class Rectangle:
#   def __init__(self, width, height):
#     self.width = width
#     self.height = height

#   @classmethod
#   def square(cls, side):
#     return cls(side, side)

# sq1 = Rectangle.square(5)
# print(sq1.width, " ", sq1.height)

''' 4.
Create a class `Date` with attributes: day, month, year
Add a class method `from_string(cls, date_str)` that takes a string like "29-07-2025"
and returns a Date object. Use `split('-')` to extract values.
Print the day, month, and year.
'''
# class Date:
#   def __init__(self, day, month, year):
#     self.day = day
#     self.month = month
#     self.year = year

#   @classmethod
#   def from_string(cls, date_str):
#     return cls(*date_str.split("-"))

# date = Date.from_string("29-07-2025")
# print(date.day, date.month, date.year)

''' 5.
Create a class `Car` with brand and model
Add a class method `default_car(cls)` that always returns a Car object
with brand = "Toyota" and model = "Corolla"
Create an object using this method and print its details.
'''
# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   @classmethod
#   def default_car(cls):
#     return cls("Toyota", "Corolla")

# car = Car.default_car()
# print(car.brand, car.model)