''' 1.
Create a class `Employee` that:
  - Has a class variable `employee_count` to track the number of employees created.
  - Has instance variables: `name` and `age`
  - Increments `employee_count` inside the constructor.
  - Has a method `show_details()` to print name and age.
Create 3 objects and print `employee_count` using the class name.
'''
# class Employee:
#   employee_count = 0
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#     Employee.employee_count += 1
#   def show_details(self):
#       print(f"Employee number {Employee.employee_count} is {self.name} and is {self.age} years old")

# Emp1 = Employee("km_abro",19)
# Emp1.show_details()
# Emp2 = Employee("abc",19)
# Emp2.show_details()
# Emp3 = Employee("xyz",19)
# Emp3.show_details()

''' 2.
Create a class `Car` with:
  - A class variable `wheels = 4`
  - An instance variable `color` set through constructor.
  - A method `info()` that prints number of wheels and color.
Create 2 cars with different colors and print their info.
Then change wheels to 6 using the class name. Print info again.
'''
# class Car:
#   wheels = 4
#   def __init__(self,color):
#     self.color = color
#   def info(self):
#     print(f"Car has {Car.wheels} wheels and is {self.color} in color")

# car1 = Car("red")
# car1.info()
# car2 = Car("blue")
# car2.info()
# car3 = Car("green")
# Car.wheels = 6
# car3.info()

''' 3.
Create a class `BankAccount` with:
  - Class variable `bank_name = "ABC Bank"`
  - Instance variables `account_holder` and `balance`
  - A method `display()` to show account holder, balance, and bank name
Create two accounts with different holders and balances.
Then change `bank_name` for one object only using: obj.bank_name = "XYZ Bank"
Call display() for both accounts. What do you observe?
'''
# class BankAccount:
#   bank_name = "ABC Bank"
#   def __init__(self,account_holder,balance):
#     self.account_holder = account_holder
#     self.balance = balance

#   def display(self):
#     print(f"Account holder is {self.account_holder} and balance is {self.balance} and bank name is {self.bank_name}")

# BA1 = BankAccount("km_abro",10000)
# BA1.display()
# BA2 = BankAccount("abc",20000)
# BA2.display()
# obj = BankAccount("xyz",30000)
# obj.bank_name = "XYZ Bank"
# obj.display()

''' 4.
Create a class `Library` with:
  - A class variable `total_books` initialized to 1000
  - An instance variable `borrowed_books` (default is 0, set in constructor)
  - A method `borrow(n)` that:
      - Increases `borrowed_books` by `n`
      - Decreases `total_books` by `n`
  - A method `status()` that prints borrowed books and total books
Create 2 members, borrow books using both, and print status.
What do you notice about `total_books`?
'''
# class Library:
#   total_books = 1000
#   def __init__(self,borrowed_books=0):
#     self.borrowed_books = borrowed_books

#   def borrow(self,n):
#     self.borrowed_books += n
#     Library.total_books -= n

#   def status(self):
#     print(f"Borrowed books are {self.borrowed_books} and total books are {Library.total_books}")

# member1 = Library()
# member2 = Library()

# member1.borrow(100)
# member1.status()
# member2.borrow(200)
# member2.status()

''' 5.
Create a class `Pet` with:
  - Class variable `species = "Dog"`
  - Instance variables `name` and `age`
  - A method `details()` to print name, age, and species
Create 2 objects. Change `species` to "Cat" **for one object only**.
Print details for both objects.
Does changing species affect the other object? Why?
'''
# class Pet:
#   species = "Dog"
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age

#   def details(self):
#     print(f"Name is {self.name} and age is {self.age} and species is {self.species}")

# obj1 = Pet("abc",19)
# obj1.details()
# obj2 = Pet("xyz",20)
# obj2.species = "Cat"
# obj2.details()

''' 6.
Create a class `Game` with:
  - Class variable `players_online = 0`
  - Instance variable `username`
  - In the constructor:
      - Assign username
      - Increment `players_online` by 1
  - A method `logout()` that:
      - Decreases `players_online` by 1
      - Prints "Player <username> logged out"
Create 3 players and show total online players.
Logout 1 player and show updated player count.
'''
# class Game:
#   players_online = 0
#   def __init__(self,username):
#     self.username = username
#     Game.players_online += 1
#     print(f"Player {self.username} logged in")
    
#   def logout(self):
#     Game.players_online -= 1
#     print(f"Player {self.username} logged out")

# ply1 = Game("km_abro")
# ply2 = Game("abc")
# ply3 = Game("xyz")
# print("Online players are:",Game.players_online)
# ply1.logout()
# print("Online players are:",Game.players_online)