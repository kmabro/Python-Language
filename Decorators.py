'''1. Write a decorator called `simple_decorator` that prints "Before call" before executing a function. 
Use it on a function `greet()` that prints "Hello!".'''
# def simple_decorator(func):
#     def wrapper():
#         print("Before call")
#         func()
#     return wrapper

# @simple_decorator
# def greet():
#     print("Hello!")

# greet()

'''2. Create a decorator `shout` that turns any returned string into uppercase. 
Use it to decorate a function `say_name()` that returns your name.'''
# def shout(func):
#   def wrapper():
#     return func().upper()
#   return wrapper
# @shout
# def say_name():
#   return "km_abro"

# print(say_name())

'''3. Make a decorator `debug` that prints the function name before it runs. 
Use it to decorate a function `add(a, b)` that returns the sum.'''
# def debug(func):
#   def wrapper(*args, **kwargs):
#     print(func.__name__)
#     return func(*args, **kwargs)
#   return wrapper

# @debug
# def add(a, b):
#   return a + b

# print(add(2, 3))

'''4. Write a decorator `double_result` that multiplies the result of a function by 2. 
Use it on a function `get_number()` that returns 5.'''
# def double_result(func):
#   def wrapper(*args, **kwargs):
#     return func(*args, **kwargs) * 2
#   return wrapper

# def get_number():
#   return 5

# print(double_result(get_number)())

'''5. Write a decorator `say_hi` that prints "Hi there!" before the decorated function runs.
Use it to decorate a function `welcome()` that prints "Welcome to Python".'''
# def say_hi(func):
#   def wrapper():
#     print("Hi there!")
#     func()
#   return wrapper

# @say_hi
# def welcome():
#   print("Welcome to Python")
  
# welcome()

'''6. Create a decorator `greet_user` that prints "Checking user..." before the function.
Decorate a function `login()` that prints "User logged in".'''
# def greet_user(func):
#   def wrapper():
#     print("Checking user...")
#     func()
#   return wrapper

# @greet_user
# def login():
#   print("User logged in")

# login()

'''7. Write a decorator `print_done` that prints "Done!" after the function is executed.
Use it on a function `task()` that prints "Doing some task...".'''
# def print_done(func):
#   def wrapper():
#     print("Done!")
#     func()
#   return wrapper

# @print_done
# def task():
#   print("Doing some task...")

# task()

'''8. Define a decorator `wrap_line` that prints a line of dashes (--------) before and after the function runs.
Use it on a function `show_message()` that prints "This is a message".'''
# def wrap_line(func):
#   def wrapper():
#     print("--------")
#     func()
#     print("--------")
#   return wrapper

# @wrap_line
# def show_message():
#   print("This is a message")

# show_message()

'''9. Make a decorator `announce` that prints "Starting..." before the function and "Finished!" after it.
Decorate a function `process()` that prints "In progress...".'''
# def announce(func):
#   def wrapper():
#       print("Starting...")
#       func()
#       print("Finished!")
#   return wrapper

# @announce
# def process():
#   print("In progress...")

# process()


'''10. Write a decorator called `smart_divide` that checks if the denominator is zero before performing division. If zero, print "Cannot divide by zero".'''
# def smart_divide(func):
#   def wrapper(a,b):
#     if b == 0:
#       print("Cannot divide by zero")
#     else:
#       return func(a,b)
#   return wrapper

# @smart_divide
# def divide(a, b):
#   return a / b

# print(divide(10, 2))


  