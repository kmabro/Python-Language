''' 1.
Create a class `Converter` with a static method `km_to_miles(km)`
that converts kilometers to miles using the formula: miles = km * 0.621371
Test the method by calling it without creating an instance of the class.
'''
# class Converter:
#   @staticmethod
#   def km_to_miles(km):
#     miles = km * 0.621371
#     return miles

# r1 = Converter.km_to_miles(10)
# print("10 km =", r1, "miles")
# r2 = Converter.km_to_miles(20)
# print("20 km =", r2, "miles")
# r3 = Converter.km_to_miles(30)
# print("30 km =", r3, "miles")

''' 2.
Create a class `Temperature` with:
  - A static method `celsius_to_fahrenheit(c)`
    that converts Celsius to Fahrenheit using: F = (C * 9/5) + 32
  - A static method `fahrenheit_to_celsius(f)`
    that converts Fahrenheit to Celsius using: C = (F - 32) * 5/9
Call both methods from the class directly and print results.
'''
# class Temperature:
#   @staticmethod  
#   def celsius_to_fahrenheit(c):
#     f = (c * 9/5) + 32
#     return f

#   @staticmethod
#   def fahrenheit_to_celsius(f):
#     c = (f - 32) * 5/9
#     return c

# CtoF = Temperature.celsius_to_fahrenheit(30)
# print("30°C =", CtoF, "F")
# FtoC = Temperature.fahrenheit_to_celsius(86)
# print("86°F =", FtoC, "C")

''' 3.
Create a class `Validator` with a static method `is_valid_email(email)`
that checks if the given email string contains "@" and "."
If both are found, return True; otherwise return False.
Call the method using the class name and test a few email strings.
'''
class Validator:
  @staticmethod
  def is_valid_email(email):
    if "@" in email and "." in email:
      return True
    else:
      return False
# e1 = Validator.is_valid_email("kmabro786110@gmail.com")
# print(e1)
# e2 = Validator.is_valid_email("kmabro786110gmail.com")
# print(e2)
# e3 = Validator.is_valid_email("kmabro786110@gmailcom")
# print(e3)

''' 4.
Create a class `MathTools` with:
  - A static method `is_prime(n)` that checks if a number is prime.
    Return True if prime, else False.
Test it with different values by calling the method using the class name.
'''
# class MathTools:
#   @staticmethod
#   def is_prime(n):
#     if n < 2:
#       return False
#     for i in range(2, int(n**0.5) + 1):
#       if n % i == 0:
#         return False
#     return True

# test_nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
# for i in test_nums:
#   print(i, "is prime:", MathTools.is_prime(i))

''' 5.
Create a class `PasswordUtils` with:
  - A static method `is_strong(password)` that returns True if the password:
    - Is at least 8 characters long
    - Contains both letters and numbers
    - Contains at least one special character (!, @, #, $, etc.)
Test it with different password strings.
'''
# class PasswordUtils:
#   @staticmethod
#   def is_strong(password):
#     if len(password) <8:
#       return False
#     if not any(char.isdigit() for char in password):
#       return False
#     if not any(char.isalpha() for char in password):
#       return False
#     if not any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for char in password):
#         return False
#     return True
# passes = ["Khan@123", "Khan123", "Khan@123456789", "Khan123456789","Khan@123456789", "Khan123456789", "Khan@123456789"]
# for i in passes:
#   print(i, "is strong:", PasswordUtils.is_strong(i))

''' 6.
Create a class `Circle` with:
  - A class variable `pi = 3.14159`
  - A static method `area(radius)` that calculates and returns area of a circle.
    Use formula: area = pi * radius * radius
(Hint: You can access `Circle.pi` inside the static method.)
Test it with different radius values.
'''
# class Circle:
#   pi = 3.14159
#   @staticmethod
#   def area(radius):
#     return Circle.pi * radius * radius

# c1 = Circle.area(10)
# print(c1)
# c2 = Circle.area(20)
# print(c2)
# c3 = Circle.area(30)
# print(c3)
# c4 = Circle.area(40)
# print(c4)
# c5 = Circle.area(50)
# print(f"{c5:.3f}")