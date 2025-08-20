'''1. Create a class named `Car` with attributes `brand` and `year`. 
Then create an object and print those values.'''
# class Car:
#   brand = "Toyota"
#   year = 2020
# Ob = Car()
# print(Ob.brand)
# print(Ob.year)

'''2. Create a class called `Animal` with two attributes: `species` and `sound`. 
Set the values inside the class (not with constructor). Then, create an object and print both attributes.'''
# class Animal:
#   species = "Dog"
#   sound = "Bark"
# Ob = Animal()
# print(Ob.species, " ", Ob.sound)

'''3. Define a class `Book` with attributes `title` and `author`. 
Create an object and print the title and author using the object.'''
# class Book:
#   title = "Python"
#   author = "Guido van Rossum"
# ob = Book()
# print(ob.title, " ", ob.author)

'''4. Create a class `Laptop` with attributes `brand` and `price`. 
Add a method `show_info` that prints "Brand: <brand>, Price: <price>". 
Create an object and call the method.'''
# class Laptop:
#   brand = "HP"
#   price = 75000
#   def show_info(self):
#     print("Brand: ", self.brand, "Price: ", self.price)
# ob = Laptop()
# ob.show_info()

'''5. Create a class `Fruit` with attributes `name` and `color`. 
Create two different objects for the class with different values. Print their attributes.'''
# class Fruit:
#   name = "Apple"
#   color = "Red"
# ob1 = Fruit()
# ob2 = Fruit()
# print(ob1.name, " ", ob1.color)
# ob2.name = "Banana"
# ob2.color = "Yellow"
# print(ob2.name, " ", ob2.color)

'''6. Write a class `Pen` with an attribute `ink_color`. 
Add a method `write` that prints "Writing with <ink_color> ink". 
Create an object and call the method.'''
# class Pen:
#   ink_color = "Blue"
#   def write(self):
#     print("Writing with ", self.ink_color, "ink")
# ob = Pen() 
# ob.write()

'''7. Create a class `City` with attribute `name`. 
Define a method `welcome` that prints "Welcome to <name>". 
Create two objects and call the method for both.'''
# class City:
#   name = "Sukkur"
#   def welcome(self):
#     print("Welcome to", self.name)
# ob = City()
# ob.welcome()

'''8. Create a class `LightBulb` with an attribute `status = "off"`. 
Add a method `turn_on` that changes status to "on" and prints the current status.'''
# class LightBulb:
#   status = "off"
#   def turn_on(self):
#     self.status = "on"
#     print("Current status:", self.status)
# ob = LightBulb()
# ob.turn_on()