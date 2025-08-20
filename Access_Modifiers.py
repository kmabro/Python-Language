''' 1.
Create a class `Employee` with public variables `name` and `salary`.
Create an object, set values in the constructor, and print both variables outside the class.
'''
# class Employee:
#   def __init__(self, name, salary):
#     self.name = name
#     self.salary = salary

# obj = Employee("Khan Muhammad", 100000)
# print("name:", obj.name)
# print("salary:", obj.salary)
''' 2.
Create a class `BankAccount` with a private variable `__balance`.
Add a method `show_balance()` to print the balance.
Try printing `__balance` directly (outside the class). What happens?
Then access it using name mangling.
'''
# class BankAccount:
#   def __init__(self, balance):
#     self.__balance = balance

#   def show_balance(self):
#     print("balance:", self.__balance)

# obj = BankAccount(100000)
# obj.show_balance()

# # print(obj.__balance) # Error

# print("name mangling:",obj._BankAccount__balance)

# print(dir(obj))
''' 3.
Create a class `Person` with a protected variable `_nationality` and a method `_show_nationality()`.
Create a child class `Citizen` that inherits from `Person`.
From the child class object, print `_nationality` and call `_show_nationality()`.
'''
# class Person:
#   def __init__(self, nationality):
#     self._nationality = nationality

#   def _show_nationality(self):
#     print("nationality:", self._nationality)

# class Citizen(Person):
#   pass

# obj = Citizen("Pakistani")
# print("nationality:", obj._nationality)
# obj._show_nationality()
''' 4.
Create a class `Laptop` with:
  - Public variable: `brand`
  - Private variable: `__serial_number`
  - Protected variable: `_model`
Add a method `display_info()` that prints all three values.
Create an object and call the method.
Try accessing each variable directly from outside. Observe what works and what doesn't.
'''
# class Laptop:
#   def __init__(self, brand, serial_number, model):
#     self.brand = brand
#     self.__serial_number = serial_number
#     self._model = model

#   def display_info(self):
#     print("brand:", self.brand)
#     print("serial_number:", self.__serial_number)
#     print("model:", self._model)

# obj = Laptop("Dell", 123456, "Inspiron")
# obj.display_info()
# print("***accessing each variable directly from outside***")
# print(obj.brand)
# print(obj._Laptop__serial_number)
# print(obj._model)
''' 5.
Create a base class `User` with a private method `__login()`.
Create a derived class `Admin` and try to call `__login()` from it.
Then use name mangling to access the private method from outside the base class.
'''
# class User:
#   def __login(self):
#     print("login")

# class Admin(User):
#   pass

# obj = Admin()
# #obj.login() # Error

# # name mangling
# obj._User__login()
''' 6.
Create a class `Student` with a private variable `__grade`.
Add a getter and setter for grade using property decorators.
Try changing the grade using the setter and print it using the getter.
'''
# class Student:
#   def __init__(self, grade):
#     self.__grade = grade

#   @property
#   def grade(self):
#     return self.__grade

#   @grade.setter
#   def grade(self, new_grade):
#     self.__grade = new_grade

# St = Student("B")
# print("grade:", St.grade)

# St.grade = "A"
# print("updated grade:", St.grade)
''' 7.
Create a class `Smartphone` with:
  - Public variable: `brand`
  - Protected variable: `_model`
  - Private variable: `__imei`
Add a method `show_details()` that prints all 3 values.
Create an object, initialize all values in the constructor, and call `show_details()`.
Try to access each variable directly from outside the class.
Try accessing the private variable using name mangling.
'''
# class Smartphone:
#   def __init__(self, brand, model, imei):
#     self.brand = brand
#     self._model = model
#     self.__imei = imei

#   def show_details(self):
#     print("brand:", self.brand)
#     print("model:", self._model)
#     print("imei:", self.__imei)

# sp = Smartphone("Samsung", "S23", 1234567890)
# sp.show_details()
# print(sp.brand)
# print(sp._model)
# print(sp._Smartphone__imei)
''' 2.
Create a class `Vehicle` with:
  - Public variable: `type`
  - Protected variable: `_engine_type`
  - Private variable: `__chassis_number`
Add a method `vehicle_info()` that prints all variables.
Then create a subclass `Car` that inherits from `Vehicle`.
In the child class, create a method `car_info()` that tries to access all three variables.
Create an object of `Car`, and call both methods.
Finally, try accessing the variables directly using the object and name mangling (for private).
'''
# class Vehicle:
#   def __init__(self, type, engine_type, chassis_number):
#     self.type = type
#     self._engine_type = engine_type
#     self.__chassis_number = chassis_number

#   def vehicle_info(self):
#     print("type:", self.type)
#     print("engine_type:", self._engine_type)
#     print("chassis_number:", self.__chassis_number)

# class Car(Vehicle):
#   def car_info(self):
#     print("type:", self.type)
#     print("engine_type:", self._engine_type)
#     print("chassis_number:",     self._Vehicle__chassis_number)

# obj = Car("SUV", "V8", 1234567890)
# obj.vehicle_info()
# obj.car_info()
# print(obj.type)
# print(obj._engine_type)
# print(obj._Vehicle__chassis_number)
