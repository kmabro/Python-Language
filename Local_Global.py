# 1.
"""
Create a function that defines a local variable `message` with the value "Hello from local!".
Print the variable inside the function. Then try printing it outside the function.
"""
# def print_message():
#     message = "Hello from local!"
#     print(message)
  # print_message()
# print(message) # name 'message' is not defined


# 2.
"""
Create a global variable `count = 0`. Define a function `increment()` that tries to add 1 to `count`.
Call the function and print `count`. Explain what happens.
"""
# count = 0
# def increment():
#   count += 1
#   print(count)
# increment() # UnboundLocalError: local variable 'count' referenced before assignment


# 3.
"""
Modify Question 2 so that the function `increment()` actually increases the global `count` using the `global` keyword.
"""
# count = 0
# def increment():
#   global count
#   count += 1
#   print(count)
# increment() 


# 4.
"""
Write a function that creates a local variable with the same name as a global variable (e.g. name = "Alice").
Show that changing the local variable inside the function does not affect the global one.
"""
# name = "Alice"
# def change_name():
#   name = "Khan Muhammad"
#   print(name)
# print(name)
# change_name()


# 5.
"""
Declare a global variable `status = "active"`.
Inside a function, use the global keyword to change its value to "inactive".
Print the value before and after calling the function.
"""
# status = "active"
# def change_status():
#   global status
#   status = "inactive"
#   print(status)
# print(status)
# change_status()


# 6.
"""
Write a function that accepts two numbers and returns their sum.
Inside the function, also define a local variable `operation = "addition"`.
Can you print `operation` from outside the function?
"""
# def add(a, b):
#   operation = "addition"
#   return a + b
# add(5, 3)
# print(operation) # NameError: name 'operation' is not defined. did you mean : 'StopIteration'?


# 7.
"""
Demonstrate the use of a local variable with the same name as a global variable (e.g. `x = 10` globally and `x = 5` locally).
Print both inside and outside the function to show they are treated separately.
"""
# x = 10
# def change_x():
#   x = 5
#   print(x)
# print(x)
# change_x()


# 8.
"""
Create a function that uses both a local variable and a global variable in a calculation.
Example: global `bonus = 100`, local `salary = 500`. Total = salary + bonus.
Return the result and print it.
"""
# bonus = 100
# def calculate_total():
#   salary = 500
#   total = salary + bonus
#   return total
# print(calculate_total())
