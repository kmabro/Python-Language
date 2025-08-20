'''# 1️⃣ Use .format() to print: "This course costs $499.99 only!"
# Hint: Use a variable inside format()
price = 499.99
# Your code here'''
# price = 499.99
# txt = "This course costs ${} only!"
# print(txt.format(price))

'''# 2️⃣ Use .format() to format the number 5.6789 up to 2 decimal places.
# Expected Output: The result is 5.68
num = 5.6789
# Your code here'''
# num = 5.6789
# txt = "The result is {:.2f}"
# print(txt.format(num))

'''# 3️⃣ Create an f-string that says:
# "User Admin has logged in from IP 192.168.1.1"
user = "Admin"
ip = "192.168.1.1"
# Your code here'''
# user = "Admin"
# ip = "192.168.1.1"
# print(f"User {user} has logged in from IP {ip}")

'''# 4️⃣ Print: "Disk usage is at 72.56%" using f-string and format specifier to 2 decimals
usage = 72.55555
# Your code here'''
# usage = 72.55555
# print(f"Disk usage is at {usage:.2f}%")

'''# 5️⃣ Use f-string to print:
# "Hi Alex, your order total is $230.75"
name = "Alex"
amount = 230.749
# Your code here'''
# name = "Alex"
# amount = 230.749
# print(f"Hi {name}, your order total is ${amount}")

'''# 6️⃣ Create a one-liner f-string that prints:
# "3 + 4 = 7"
# (No variables needed)
# Your code here'''
# print(f"3 + 4 = {3+4}")

'''# 7️⃣ CYBERSECURITY CONTEXT:
# Use f-string to print:
# "Alert: 5 login attempts detected from IP 10.0.0.7"
ip = "10.0.0.7"
attempts = 5
# Your code here'''
# ip = "10.0.0.7"
# attempts = 5
# print(f"Alert: {attempts} login attempts detected from IP {ip}")


##### DOCSTRING & pep8 #####


# def square(n):
#     '''Takes in a number n, returns the square of n'''
#     print(n**2)
# square(5)
# print(square.__doc__)

'''# 1️⃣ Define a function `greet(name)` that prints "Hello, <name>!"
# Add a one-line docstring describing what the function does.
# Then, print its __doc__ value.
# Expected Output: The docstring content'''
# def greet(name):
#     '''Prints "Hello, <name>!"'''
#     print(f"Hello, {name}!")
# greet("Khan Muhammad")
# print(greet.__doc__)

'''# 2️⃣ Create a function `multiply(x, y)` with a multi-line docstring
# Docstring should explain parameters, return value, and give one example.
# Return the result and then print the docstring using __doc__'''
# def multiply(x, y):
#     '''This function takes two parameters x and y, and returns their product.
#     Example:
#     multiply(3, 4) -> 12'''
#     return x * y #print(x*y)
# print(multiply(3, 4))
# print(multiply.__doc__)

'''# 3️⃣ Create a function `check_even(n)` with a docstring.
# Return True if number is even, otherwise False.
# Then call help(check_even) to view the docstring as documentation.'''
# def check_even(n):
#     '''This function takes a number n and returns True if the number is even, otherwise False.'''
#     return n % 2 == 0
# print(f"check_even for 4: {check_even(4)}")
# print(f"check_even for 5: {check_even(5)}")
# print(check_even.__doc__)

'''# 4️⃣ CYBERSECURITY CONTEXT:
# Create a function `log_event(ip, event)` that prints a log message.
# Add a docstring explaining it logs a cybersecurity event.
# Call the function and print its docstring using __doc__'''
# def log_event(ip, event):
#     '''This function logs a cybersecurity event by printing a message with the IP address and the event.'''
#     print(f"Event '{event}' detected from IP {ip}") 
# log_event("192.168.1.1", "Unauthorized access attempt")
# print(log_event.__doc__)

'''# 5️⃣ PEP8 Practice:
# Read this code and correct it to follow PEP8 style guidelines:
def  sum ( a,b):return a+b
print(sum(3,4))'''
# def sum(a, b):
#     return a + b
# print(sum(3, 4))

'''# 6️⃣ Write a docstring inside a class definition `Device`
# The docstring should explain that this class stores device info like name and IP.
# Then use print(Device.__doc__) to display it.'''
# def Device():
#     '''This class stores device info like name and IP.'''
# print(Device.__doc__)

'''# 7️⃣ Import the Zen of Python and read the output.
# What line do you find the most meaningful?
import this'''
# import this
# print(this)
# '''"If the implementation is hard to explain, it's a bad idea. 
# If the implementation is easy to explain, it may be a good idea."'''

'''# 8️⃣ Create a function `secure_hash(data)` with a docstring that:
# - Mentions its purpose (e.g., for hashing secure data)
# - Mentions required input type
# Return "HASHED_" + data
# Print its docstring'''
# def secure_hash(data):
#     '''This function is for hashing secure data. It takes a string data as input and returns "HASHED_" + data.'''
#     return "HASHED_" + data
# print(secure_hash("password123"))
# print(secure_hash.__doc__)