'''Write a Python program that imports only the sqrt function from the math module and prints the square root of 121.'''
# from math import sqrt
# print(sqrt(121))

'''Import the math module as m and use it to print the value of pi and the cosine of 0.'''
# import math as m
# print("Value of pi: ",m.pi)
# print("Cosine of 0: ",m.cos(0))

'''Write a program that prints all available names (functions, constants) in the math module using the dir() function.'''
# import math
# print(dir(math))

'''Import both pi and pow from the math module and print the value of pi and 2^5'''
# from math import pi, pow
# print("Value of pi: ",pi)
# print("2^5: ",pow(2,5))

'''Import everything from the math module using *, then print the sine of pi/2.'''
# from math import *
# print("Sine of pi/2: ",sin(pi/2))

'''Suppose you have a file named greetings.py containing:
# greetings.py
def say_hello():
    print("Hello from greetings module!")

Write a script that imports and calls say_hello() from greetings.'''
# from greetings import say_hello
# say_hello()

'''Using the greetings.py module from previous question, print all its defined names using dir().'''
# import greetings  
# print(dir(greetings))

'''You have a file info.py:
# info.py
name = "Khan"
def welcome():
    print("Welcome", name)

Import both name and welcome from info.py and use them in a script.'''
# from info import name, welcome
# print(name)
# welcome()



##### if "__name__ == "__main__" #####


# 1.
"""
Create a script with a function `greet()` that prints "Hello from main". 
Use `if __name__ == "__main__"` to call `greet()` only when run directly. 
Then import this file into another script and check that `greet()` doesn't run automatically."""
# from scripts import greet
# greet()

# 2.
"""
Create a script with two functions: `add(a, b)` and `sub(a, b)`. 
Use `if __name__ == "__main__"` to only run `add()` with example values when the script is executed directly.
"""
# from scripts import add, sub
# add(4,5)
# sub(4,5)

# 3.
"""
Create a module called `scripts.py` that has a `welcome()` function and a main guard 
so that `welcome()` runs only when the file is executed directly.
Then create a second script that imports `scripts` and calls `scripts.welcome()`.
Make sure `welcome()` runs only once.
"""
# from scripts import welcome
# welcome()

