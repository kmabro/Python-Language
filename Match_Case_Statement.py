'''# Input a number from 1 to 7 and print the corresponding day name using match-case.
# 1 → Monday, 2 → Tuesday, ..., 7 → Sunday'''
# day = int(input("Enter a number from 1 to 7: "))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid input")

'''# Input a color ("red", "yellow", "green")
# Use match-case to print:
# - "Stop" for red
# - "Slow down" for yellow
# - "Go" for green
# - "Invalid color" for any other input'''
# color = input("Enter a color (red, yellow, green): ").lower()
# match color:
#     case "red":
#       print("Stop")
#     case "yellow":
#       print("Slow down")
#     case "green":
#       print("Go")
#     case _:
#       print("Invalid color")

'''# Input two numbers and an operator (+, -, *, /)
# Use match-case to perform the operation and print result'''
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# op = input("Enter an operator (+, -, *, /): ")
# match op:
#     case "+":
#       print(num1 + num2)
#     case "-":
#       print(num1 - num2)
#     case "*":
#       print(num1 * num2)
#     case "/":
#       print(num1 / num2)
#     case _:
#       print("Invalid operator")

'''# Input a single character and use match-case to check:
# - if it's a vowel (a, e, i, o, u)
# - else it's a consonant'''
# char = input("Enter a single character: ").lower()
# match char:
#       case "a"|"e"|"i"|"o"|"u":
#         print("Vowel")
#       case _:
#         print("Consonant")

'''# Input a score (0-100) and print grade using match-case:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# below 60: F'''
# score = float(input("Enter a score (0-100): "))
# match True:
#     case _ if 90 <= score <= 100:
#         print("A")
#     case _ if 80 <= score < 90:
#         print("B")
#     case _ if 70 <= score < 80:
#         print("C")
#     case _ if 60 <= score < 70:
#         print("D")
#     case _ if 0 <= score < 60:
#         print("F")
#     case _:
#         print("Invalid score")

'''# Create a match-case menu:
# 1. Start
# 2. Settings
# 3. Quit
# If input is anything else → "Invalid selection"'''
# while True:
#     user = input("Enter a number (1: Start, 2: Settings, 3: Quit): ").strip()
#     match user:
#         case "1":
#             print("Start")
#         case "2":
#             print("Settings")
#         case "3":
#             print("Quit")
#             break
#         case _:
#             print("Invalid selection")
