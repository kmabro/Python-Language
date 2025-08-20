##### Exception Handling #####

'''# 1️⃣ Simple: Ask the user to enter a number and print its square.
# Handle the case if the input is not a number.

# Use try-except for ValueError'''
# num = input("Enter a number: ")
# try:
#   num = int(num)
#   print(num*num)
# except ValueError:
#   print("Invalid input")

'''# 2️⃣ Create a program that divides two numbers entered by the user.
# Handle both ValueError (invalid input) and ZeroDivisionError (dividing by zero).'''
# num1 = input("Enter a divisor: ")
# num2 = input("Enter a dividend: ")
# try:
#   num1 = int(num1)
#   num2 = int(num2)
#   print(f"{num1/num2:.2f}")
# except ValueError:
#   print("Invalid input")
# except ZeroDivisionError:
#   print("Cannot divide by zero")

'''# 3️⃣ Ask the user to input an index and access that index from a list.
# Handle IndexError if index is out of bounds.'''
# nums = (1,2,3,4,5)
# index = input("Enter an index: ")
# try:
#   index = int(index)
#   print(nums[index])
# except IndexError:
#   print("Index out of bounds")

'''# 4️⃣ Prompt the user to enter a filename.
# Attempt to open and read it.
# Handle FileNotFoundError if the file does not exist.'''
# filename = input("Enter a filename: ")
# try:
#   with open(filename, 'r') as file:
#     print(file.read())
# except FileNotFoundError:
#   print("File not found")

'''# 5️⃣ Use `try-except-else-finally`:
# Ask for a number and divide 100 by that number.
# Print success message in else, and always print "Done" in finally.'''
# num = input("Enter a number: ")
# try:
#   num = int(num)
#   result = 100 / num
# except ValueError:
#   print("Invalid input")
# else:
#   print(f"Result: {result}")
# finally:
#   print("Done")

'''# 6️⃣ Loop to keep asking user for a valid number until correct input is given.
# Use exception handling to repeat the prompt until a valid integer is entered.'''
# while(True):
#   num = input("Enter a number: ")
#   try:
#     num = int(num)
#     print(f"Your number is {num}")
#     break
#   except ValueError:
#     print("Invalid input, try again")

'''# 7️⃣ Cybersecurity Twist:
# Simulate reading a suspicious file that may be missing or unreadable.
# Ask for a filename and handle file-related exceptions (FileNotFoundError, PermissionError).'''
# f_n = input("Enter a filename: ")
# try:
#   with open(f_n, 'r') as file:
#     print(file.read())
# except FileNotFoundError:
#   print("File not found")
# except PermissionError:
#   print("Permission denied")

##### Finally Keyword #####

'''# 1️⃣ Ask the user to input two numbers and divide them.
# Use finally to always print "Division operation complete."'''
# num1 = input("Enter a dividend number: ")
# num2 = input("Enter a divisor number: ")
# try:
#   print(int(num1)/int(num2))
# except ValueError:
#   print("Invalid input")
# except ZeroDivisionError:
#   print("Cannot divide by zero")
# finally:
#   print("Division operation complete")

'''# 2️⃣ Try to access an index in a list using user input.
# Catch IndexError and always print the full list in finally block.'''
# nums = [1,2,3,4,5]
# try:
#   print(nums[int(input("Enter an index: "))])
# except IndexError:
#   print("Index out of bounds")
# finally:
#   print(nums)

'''# 3️⃣ Create a login simulation:
# User must enter correct password ('python123').
# After attempt, whether correct or wrong, print "Attempt finished." using finally.'''
# c_p = "python123"
# password = input("Enter password: ")
# try:
#     if password != c_p:
#         print("Incorrect password")
#     else:
#         print("Login successful")
# finally:
#     print("Attempt finished")

'''# 4️⃣ Ask the user to enter a number.
# Raise a ValueError if the number is negative.
# Print "Execution done." in finally.'''
# num = int(input("Enter a positive number: "))
# try:
#     if num < 0:
#         print("Negative number entered")
#     else:
#         print("Number accepted:", num)
# finally:
#     print("Execution done.")

'''# 5️⃣ Cybersecurity Twist:
# Simulate a login system with a `try-except-finally` where:
# - If password wrong, raise Exception
# - Catch it and show "Invalid login"
# - Always log "Login attempt ended" using finally'''
# c_p = '123'
# password = input("Enter password: ")
# try:
#     if password != c_p:
#         print("Invalid login")
#     else:
#         print("Login successful")
# except Exception:
#     print("An error occurred")
# finally:
#     print("Login attempt ended")


##### RAISING CUSTOM ERRORS #####

'''# 1️⃣ Ask the user for their age.
# Raise a ValueError if age is not between 1 and 120.'''
# age = int(input("Enter your age: "))
# if age < 1 or age > 120:
#     raise ValueError("Invalid age")
# print("Valid age:", age)

'''# 2️⃣ Ask the user to enter a password.
# Raise a custom error `WeakPasswordError` if the password is shorter than 6 characters.'''
# password = input("Enter a password: ")
# if len(password) < 6:
#     raise Exception("WeakPasswordError: Password must be at least 6 characters long")
# print("Password accepted:",password)

'''# 3️⃣ Create a function `set_salary(sal)` that raises a ValueError 
# if salary is not between 2000 and 5000.'''
# def set_salary(sal):
#     if sal < 2000 or sal > 5000:
#         raise ValueError("Salary must be between 2000 and 5000")
#     else:
#         print("Salary set successfully",sal)
# set_salary(5000)

'''# 4️⃣ Create a custom exception called `InvalidInputError`.
# Ask the user for a number and raise `InvalidInputError` if the number is not divisible by 3.'''
# num = int(input("Enter a number: "))
# if num % 3 != 0:
#     raise Exception("InvalidInputError: Number must be divisible by 3")
# else:
#     print("Number accepted:",num)  

'''# 5️⃣ Define a class `EmptyStringError`.
# Ask the user to input their name. Raise `EmptyStringError` if the input is empty.'''
# class EmptyStringError(Exception):
#   pass

# name = input("Enter your name: ")
# if name == "":
#   raise EmptyStringError("Name cannot be empty")
# else:
#   print("Name accepted:", name)

'''# 6️⃣ Define a function `withdraw(amount)` that raises a `LowBalanceError` 
# if amount > balance (use balance = 5000).'''
# def withdraw(amount):
#     balance = 5000
#     if amount > balance:
#         raise Exception("LowBalanceError: Insufficient balance")
#     else:
#         print("Withdrawal successful")
# withdraw(5000)

'''# 7️⃣ Cybersecurity Twist:
# Simulate a login system.
# Raise a `LoginFailedError` if username or password is incorrect.
# Always print "Security log updated." in a finally block.'''
# username = input("Enter username: ")
# password = input("Enter password: ")
# if username != "admin" or password != "admin123":
#     raise Exception("LoginFailedError: Invalid username or password")
# else:
#   print("Login successful")

