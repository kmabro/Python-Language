'''1. Create a class `Student` that uses a default constructor to print "Welcome to Python class!". 
Create an object and observe the message.'''
# class Student:
#   def __init__(self):
#     print("Welcome to Python class!")
# ob = Student()

'''2. Create a class `Vehicle` with a parameterized constructor that accepts `type` and `color` as arguments. 
When an object is created, it should print: "<color> <type> created!".'''
# class Vehicle:
#   def __init__(self,type,color):
#     self.type = type
#     self.color = color

#   def show_info(self):
#     print(self.color, self.type, "created!")

# ob = Vehicle("Car","Red")
# ob.show_info()

'''3. Write a class `Mobile` with a constructor that accepts `brand` and `price`. 
Create two objects with different values and print their details using a method `show_info()`.'''
# class Mobile:
#   def __init__(self,brand,price):
#     self.brand = brand
#     self.price = price
#   def show_info(self):
#     print("Price of" ,self.brand, "is", self.price)
# ob1 = Mobile("Oppo A54", 28000)
# ob1.show_info()

'''4. Define a class `Country` with a constructor that sets the `name` and `continent`. 
Also add a method `describe` that prints: "<name> is in <continent>". 
# Create and test one object.'''
# class Country:
#   def __init__(self,name,continent):
#     self.name = name
#     self.continent = continent
#   def describe(self):
#     print(self.name, "is in", self.continent)
# ob = Country("Pakistan", "Asia")
# ob.describe()

'''5. Create a class `App` with a default constructor that prints "Launching App..." 
and a method `greet()` that prints "Hello from the app!". 
Create an object and call `greet()`.'''
# class App:
#   def __init__(self):
#     print("Launching App...")
#   def greet(self):
#     print("Hello from the app!")
# ob = App()
# ob.greet()

'''6. Create a class `BankAccount` that uses a parameterized constructor to set the account holder's name and balance. 
Add a method `display()` to print the account info. Create an object and display it.'''
# class BankAccount:
#   def __init__(self,name,balance):
#     self.name = name
#     self.balance = balance
#   def display(self):
#     print("Account Holder Name:", self.name)
#     print("Balance:", self.balance)
# ob = BankAccount("Khan Muhammad", 0)
# ob.display()

'''7. Write a class `Game` with a constructor that takes `title` and `genre`. 
Create an object and print: "Game '<title>' is of genre '<genre>'".'''
# class Game:
#   def __init__(self,title,genre):
#     self.title = title
#     self.genre = genre
#     print("Game", self.title, "is of genre", self.genre)
# ob = Game("Cricket", "Sports")
