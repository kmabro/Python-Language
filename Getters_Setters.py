# class Rectangle:
#   def __init__(self, width, height):
#       self._width = width
#       self._height = height

#   @property
#   def width(self):
#       return f"{self._width:.1f} cm"

#   @property
#   def height(self):
#       return f"{self._height:.1f} cm"

#   @width.setter
#   def width(self, new_width):
#     if new_width > 0:
#       self._width = new_width
#     else:
#       print("Width must be positive")
            
#   @height.setter
#   def height(self, new_height):
#     if new_height > 0:
#       self._height = new_height
#     else:
#       print("Height must be positive")
  
# rect = Rectangle(3, 4)
# rect.width = 5
# rect.height = 6
# print(rect.width)  
# print(rect.height) 

''' 1. 
Create a class Car with a private variable _speed.
Add a getter to return the speed.
Add a setter to update the speed.
Test by printing speed before and after updating.
'''
# class Car:
#   def __init__(self,speed):
#     self._speed = speed

#   @property
#   def speed(self):
#     return f"{self._speed:.1f} km/h"

#   @speed.setter
#   def speed(self,new_speed):
#     if new_speed > 0:
#       self._speed = new_speed
#     else:
#       print("Speed must be positive")

# car = Car(100)
# print(f"Initial speed: {car.speed}")  # Print before updating
# car.speed = 150
# print(f"Updated speed: {car.speed}")  # Print after updating

''' 2. 
Create a class Temperature with private variable _celsius.
Add getter and setter to access and update celsius.
Also, add another getter called fahrenheit that returns converted value in °F.
'''
# class Temperature:
#   def __init__(self,celsius):
#       self._celsius = celsius

#   @property
#   def celsius(self):
#       return f"{self._celsius:.1f}C"

#   @celsius.setter
#   def celsius(self, new_celsius):
#       self._celsius = new_celsius

#   @property
#   def fahrenheit(self):
#       fahrenheit_value = (self._celsius * 9/5) + 32
#       return f"{fahrenheit_value:.1f}F"

# temp = Temperature(43)
# print(temp.celsius)
# print(temp.fahrenheit)

# print("After updating")
# temp.celsius = 47
# print(temp.celsius)
# print(temp.fahrenheit)

''' 3. 
Create a class Student with private variable _marks.
Allow reading and updating marks only using getter and setter.
If marks < 0, setter should raise an error.
'''
# class Student:
#   def __init__(self,marks):
#       self._marks = marks

#   @property
#   def marks(self):
#       return f"total marks are: {self._marks}"

#   @marks.setter
#   def marks(self,new_marks):
#       if new_marks >= 0:
#           self._marks = new_marks
#       else:
#           raise ValueError("Marks can't be negative")

# st = Student(95)
# print(st.marks)

# st.marks = 97
# print(st.marks)

''' 4. 
Create a class Account with a private variable _balance.
Allow only getter for balance (no setter).
'''
# class Account:
#   def __init__(self,balance):
#       self._balance = balance

#   @property
#   def balance(self):
#       return f"your balance is: {self._balance}"

# acc = Account(9500)
# print(acc.balance)

''' 5.
Create a class Product with private variables _name and _price.
Add getter and setter for price.
In the setter, raise a ValueError if price is zero or negative.
Add a getter for name but no setter (read-only).
'''
# class Product:
#   def __init__(self,name,price):
#       self._name = name
#       self._price = price

#   @property
#   def price(self):
#       return f"price is: {self._price}"
    
#   @price.setter
#   def price(self,new_price):
#     if new_price > 0:
#       self._price = new_price
#     else:
#       print("Price must be positive")

#   @property
#   def name(self):
#       return f"product name is: {self._name}"

# pro = Product("laptop",75000)
# print(pro.name)
# print(pro.price)

# print("***updated price***")
# pro.price = 80000
# print(pro.price)

''' 6. 
Create a class BankAccount with private variables _account_holder and _balance.
Add:
- Getter for account_holder (read-only)
- Getter and setter for balance
- In setter, prevent setting balance below 1000 (minimum balance)
'''
# class BankAccount:
#   def __init__(self,account_holder,balance):
#       self._account_holder = account_holder
#       self._balance = balance

#   @property
#   def account_holder(self):
#       return f"Account holder is: {self._account_holder}"

#   @property
#   def balance(self):
#       return f"Account balance is: {self._balance}"

#   @balance.setter
#   def balance(self, new_balance):
#       if new_balance >= 1000:
#           self._balance = new_balance
#       else:
#           print("Error: Minimum balance must be 1000")

# account =  BankAccount("Khan Muhammad", 1000)
# print(account.account_holder)
# print(account.balance)

# account.balance = 100000
# print("***Updated balance***")
# print(account.balance)

''' 7. 
Create a class Rectangle with private variables _length and _width.
Add:
- Getters and setters for both attributes
- A computed getter area that returns the area of the rectangle (length * width)
In setters, prevent negative values.
'''
# class Rectangle:
#   def __init__(self,length,height):
#     self._length = length
#     self._height = height

#   @property
#   def length(self):
#     return f"length is: {self._length}"

#   @property
#   def height(self):
#     return f"height is: {self._height}"

#   @length.setter
#   def length(self,new_length):
#     if new_length > 0:  
#       self._length = new_length
#     else:
#       print("Length must be positive")

#   @height.setter
#   def height(self,new_height):
#     if new_height > 0:
#       self._height = new_height
#     else:
#       print("Height must be positive")

#   @property
#   def area(self):
#     return f"Area is: {self._length * self._height}"

# rect = Rectangle(10,20)
# print(rect.length)
# print(rect.height)
# print(rect.area)

# print("***Updated Area***")
# rect.length = 15
# rect.height = 15
# print(rect.length)
# print(rect.height)
# print(rect.area)