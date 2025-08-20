'''Ask the user for their age and categorize them:
0-12: Child
13-19: Teenager
20-35: Young Adult
36-60: Adult
61+: Senior
Use if-elif-else blocks for this.'''
# age = int(input("Enter your age: "))
# if age <= 12:
#   print("Child")
# elif age <= 19:
#   print("Teenager")
# elif age <= 35:
#   print("Young Adult")
# elif age <= 60:
#   print("Adult")
# else:
#     print("Senior")

'''Ask the user for a number.
If it’s even, check:
If it's also a multiple of 4, print "Even and divisible by 4"
Else just print "Even"
If it's odd, print "Odd"
Use nested if inside else.'''
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#   if num % 4 == 0:
#     print("Even and divisible by 4")
#   else:
#     print("Even")
# else:
#   print("Odd")

'''Input a score (0–100) and print:

90–100: Grade A

80–89: Grade B

70–79: Grade C

60–69: Grade D

<60: Fail

Handle invalid input (e.g., >100 or <0)'''
# score = int(input("Enter your score: "))
# if(score>=90 and score<=100):
#   print("Grade A")
# elif(score>=80 and score<=89):
#   print("Grade B")
# elif(score>=70 and score<=79):
#   print("Grade C")
# elif(score>=60 and score<=69):
#   print("Grade D")
# elif(score<60):
#   print("Fail")
# else:
#   print("Invalid input")

'''Ask the user for username and password.

If username is "admin" and password is "1234", print "Access Granted".

If username is correct but password is wrong, print "Incorrect password".

If username is wrong, print "Unknown user".'''
# name= input("Enter your username: ")
# password= input("Enter your password: ")

# if(name == "admin" and password == "1234"):
#   print("Access Granted")
# elif(name == "admin" and password != "1234"):
#   print("Incorrect password")
# elif(name != "admin"):
#   print("Unknown user")

'''Input three side lengths and check:

If all sides are equal → "Equilateral Triangle"

If two sides are equal → "Isosceles Triangle"

If all sides are different → "Scalene Triangle"

If not a valid triangle (violates triangle inequality), print: "Not a triangle"'''
# l1 = float(input("Enter the first side: "))
# l2 = float(input("Enter the second side: "))
# l3 = float(input("Enter the third side: "))
# if(l1==l2==l3):
#   print("Equilateral Triangle")
# elif(l1==l2 or l2==l3 or l1==l3):
#   print("Isosceles Triangle")
# elif(l1!=l2!=l3):
#   print("Scalene Triangle")
# else:
#   print("Not a triangle")

'''Input a year and check:

If it is a leap year, print "Leap Year"

Else print "Not a Leap Year"

Use the leap year rules:

year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)'''
# year = int(input("Enter a year: "))
# if(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
#   print("Leap Year")
# else:
#   print("Not a Leap Year")

'''Ask for a withdrawal amount:

If amount is less than balance, and is a multiple of 500 or 1000 → Allow withdrawal

Else → Print the appropriate message: "Insufficient balance" or "Invalid amount"'''
# amount = float(input("Enter the withdrawal amount: "))
# balance = 5000
# if(amount<balance and (amount%500==0 or amount%1000==0)):
#   print("Allow withdrawal")
# else:
#   print("Insufficient balance")

'''Input a temperature in °F and:

If temp < 95 → "Hypothermia"

If temp is 96-99 → "Normal"

If temp is 100-102 → "Mild Fever"

If temp > 102 → "High Fever"'''
# F = float(input("Enter the temperature in °F: "))
# if(F<95):
#   print("Hypothermia")
# elif(F>=96 and F<=99):
#   print("Normal")
# elif(F>=100 and F<=102):
#   print("Mild Fever")
# elif(F>102):
#   print("High Fever")
# else:
#   print("Invalid input")

'''Ask the user:

Choose operation: add, subtract, multiply, divide

Then ask for two numbers

Perform the operation using if-elif-else and show result

If operation is invalid, print errorAsk the user:

Choose operation: add, subtract, multiply, divide

Then ask for two numbers

Perform the operation using if-elif-else and show result

If operation is invalid, print error'''
# op = input("Choose operation = +,-,*,/: ")
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# if(op=="+"):
#   print(num1+num2)
# elif(op=="-"):
#   print(num1-num2)
# elif(op=="*"):
#   print(num1*num2)
# elif(op=="/"):
#   print(num1/num2)
# else:
#   print("Invalid operation")

'''Ask the user for:

Age

Vision Score (out of 10)

Check:

If age ≥ 18 and vision ≥ 7 → "Eligible for license"

Else if age < 18 → "Underage"

Else → "Improve your vision"'''
# age = int(input("Enter your age: "))
# vision = float(input("Enter your vision score (out of 10): "))
# if(age>=18 and vision>=7):
#   print("Eligible for license")
# elif(age<18):
#   print("Underage")
# else:
#   print("Improve your vision")




# import time

# hour = time.strftime('%H')
# minute = time.strftime('%M')
# second = time.strftime('%S')

# print("Hour:", hour)
# print("Minute:", minute)
# print("Second:", second)

# current_time = time.strftime('%H:%M:%S')
# print("Current Time:", current_time)


##### Shorthand IF-ELSE #####

'''# Q1. Print "Even" if number is even, else print "Odd"
# Your code here'''
# num = int(input("Enter a number: "))
# print("Even") if num%2==0 else print("Odd")

'''# Q2. Assign the greater of a and b to variable max_val using one-line if-else
a = 7
b = 9
# Your code here'''
# a = 7
# b = 9
# max_val = a if a>b else b
# print(max_val)

'''# Q3. Print "Positive", "Zero", or "Negative" using nested one-line if-else
# Your code here'''
# n = int(input("Enter a number: "))
# print("Positive") if n>0 else print("Zero") if n==0 else print("Negative")

'''# Q4. Print the smaller of x and y using a one-liner
x = 23
y = 18
# Your code here'''
# x = 23
# y = 18
# print(x) if x<y else print(y)

'''# Q5. Assign "Adult" or "Minor" to variable 'status' based on age >= 18
age = 20
# Your code here'''
# age = 20
# status = "Adult" if age>=18 else "Minor"
# print(status)

'''# Q6. Set result to "Pass" if marks >= 33, "Topper" if marks >= 90, otherwise "Fail"
marks = 91
# Your code here'''
# marks = 91
# print("Topper") if marks>=90 else print("Pass") if marks>=33 else print("Fail")

'''# Q7. Print "Leap Year" if year is divisible by 4 and not by 100, or divisible by 400; else "Not Leap"
year = 2024
# Your code here'''
# year = 2024
# print("Leap Year") if year%4==0 and (year%100!=0 or year%400==0) else print("Not Leap")

'''# Q8. Given three numbers, print the largest using nested one-line if-else
a = 3
b = 9
c = 5
# Your code here'''
# a = 3
# b = 9
# c = 5
# print(a) if a>b and a>c else print(b) if b>c and b>a else print(c) 