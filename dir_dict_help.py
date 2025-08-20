'''
Create a list `my_list = [1, 2, 3]`
Use the dir() function to print all available methods and attributes of this list.
'''
# my_list = [1, 2, 3]
# print(dir(my_list))
# print("\n\n\nto add 4,5 in list")
# print(my_list.__add__([4, 5]))

'''Create a class `Car` with attributes: brand and model in the constructor
Create an object of Car and use `__dict__` to print the instance attributes
'''
# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

# car = Car("Toyota", "Corolla")
# print(car.__dict__)

'''
Use the help() function on the `list` object to see its documentation
Example: help(list)
You do not need to write a class — just call help() and observe the output
'''
# print(help(list))

'''
Define a class `Animal` with a method `speak()`
Create an object and use dir() to see available methods and attributes
'''
# class Animal:
#   def speak(self):
#     print("Animal speaks")

# animal = Animal()
# print(dir(animal))

'''
Define a class `Book` with title and author attributes
Create a `Book` object and use:
- `dir()` to list methods
- `__dict__` to show data
- `help()` on the class to see the docstring/help
'''
# class Book:
#   def __init__(self, title, author):
#     self.title = title
#     self.author = author

# book = Book("Python", "Guido")
# print("***dir***\n\n\n")
# print(dir(book))
# print("***__dict__***\n\n\n")
# print(book.__dict__)
# print("***help***\n\n\n")
# print(help(Book))

