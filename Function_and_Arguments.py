'''# Write a function named greet() that prints "Welcome to Python!" when called.'''
# def greet():
#     print("Welcome to Python!")
# greet()

'''# Write a function called full_name(first, last) that prints the full name like "Hello, John Doe".'''
# def full_name():
#     first = input("Enter your first name: ").strip()
#     last = input("Enter your last name: ").strip()
#     print("Hello,",first,last)
# full_name()

'''# Write a function that takes two numbers as input and returns their sum.'''
# def sum():
#   num1 = float(input("Enter first number: "))
#   num2 = float(input("Enter second number: "))
#   print(num1+num2)
# sum()

'''# Write a function that takes a number and prints whether it is even or odd.'''
# def even_odd():
#   num = int(input("Enter a number: "))
#   if num % 2 == 0:
#     print("Even")
#   else:
#     print("Odd")
# even_odd()

'''# Ask the user to enter a string and print its length using the len() function.'''
# str = input("Enter a string: ")
# L = len(str)
# print(L)

'''# Write a function that takes 3 numbers and prints the smallest using min().'''
'''# Write a function that takes 3 numbers and prints the smallest using min().'''
# def find_smallest():
#     n1 = int(input("Enter first number: "))
#     n2 = int(input("Enter second number: "))
#     n3 = int(input("Enter third number: "))
#     mini = min(n1, n2, n3)
#     print(mini) 
# find_smallest()

'''# Write a function that takes a list and returns a set with unique elements.'''
# def get_unique_elements(input_list):
#   return set(input_list)
# result = get_unique_elements([1, 2, 2, 3, 3, 4, 1])
# print(result)

'''# Write a function that takes a number n and returns its factorial using a loop.'''
# def fact():
#     num = int(input("Enter a number: "))
#     fact = 1
#     for i in range(1, num + 1):
#         fact = fact * i
#     print(fact)
# fact()

'''# Write a function that checks whether a given string is a palindrome.'''
# def pal():
#     str = input("Enter a string: ")
#     if str == str[::-1]:
#         print("Palindrome")
#     else:
#         print("Not Palindrome")
# pal()

'''# Write a function that takes a list of numbers and returns the average using sum() and len().'''
# def nums():
#     num = [1, 2, 3, 4, 5]
#     avg = sum(num) / len(num)
#     print(avg)
# nums()

'''Create a function greet that takes two arguments: name and greeting, where greeting should default to "Hello".
Call it with and without the second argument.'''
# def greet(name, greeting = "Hello"):
#     print(greeting, name)
# greet("Khan Muhammad")

'''Define a function full_name(fname, lname) and call it using keyword arguments in reverse order.'''
# def full_name(fname,lname):
#   print(fname,lname)
# full_name(lname="Khan",fname="Muhammad")

''''Create a function add(a, b, c) and call it with:

All three arguments

Only two arguments (see what error it throws)'''
# def add(a,b,c):
#     print(a+b+c)
#     #return a+b+c
# add(1,2,3)
# #print(add(1,2,3))

'''Create a function total_marks(*marks) that accepts any number of subject marks and returns the total.'''
# def total_marks(*marks):
#     total = sum(marks)
#     return total
# print(total_marks(90,97,95,93,83))
#####Alternative Code (Without sum())######
# def total_marks(*marks):
#     total = 0
#     for mark in marks:
#         total += mark
#     return total
# print(total_marks(90,97,95,93,83))

'''Write a function area_circle(radius) that returns the area of a circle using the formula π * r^2.'''
# def area_circle(radius):
#     return 3.14 * radius**2      # π = 3.14
#     #return 3.14 *radius * radius
# print(area_circle(5))

'''Create a function order_summary(item, quantity=1, price=100) that returns the total price. Try calling it with:

All arguments

Only item

item and quantity'''
# def order_summary(item, quantity=1, price=100):
#     return quantity * price
# print(order_summary("Apple", 5, 150))

'''Write a function longest_name(*names) that returns the longest name from the given list of names.'''
# def longest_name(*names):
#     longest = ""
#     for name in names:
#         if len(name) > len(longest):
#             longest = name
#     return longest
# print(longest_name("Khan","Muhammad","Abro","Khan Muhammad", "Khan Muhammad Abro"))

'''Write a function get_sum() that:

Asks the user to enter 3 numbers

Returns their sum'''
# def get_sum():
#   num1 = input("Enter first number: ")
#   num2 = input("Enter second number: ")
#   num3 = input("Enter third number: ")
#   return float(num1) + float(num2) + float(num3)
# print(get_sum())
