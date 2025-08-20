# name = "Khan Muhammad"
# for i in name:
#   print(i)
#   if(i=="n"):
#       print("\nstart of 2nd name")


# colors = ["Red", "Green", "Blue", "Yellow"]
# for x in colors:
#     print(x)
#     for i in x:
#       print(i)


# print("First 100 natural numbers:")
# for i in range(1,101):
#   print(i)


'''# Input your name and print each character separated by a dash ("-")
# Example:
# Input: Khan
# Output: K-h-a-n'''
# name = input("Enter your first name: ").strip()
# for i in name:
#   print(i, end="-")

# '''# Use a for loop with range() to print all even numbers between 1 and 20'''
# for i in range(2,21,2):
#   print(i)

'''# Input a number n, and calculate the sum of first n natural numbers
# Example:
# Input: 5
# Output: 15 (1+2+3+4+5)'''
# n = int(input("Enter a number to print the sum of first n natural numbers: ").strip())
# sum = 0
# if n<0:
#   print("Enter a positive number")
# else:
#   for i in range(1,n+1):
#     sum += i
#   print(sum)

'''# Print numbers from 10 to 1 using range() in reverse
# Output: 10 9 8 7 6 5 4 3 2 1'''
# for i in range(10,0,-1):
#   print(i,end=" ")

'''# Input a number and print its multiplication table up to 10
# Example:
# Input: 3
# Output: 3 6 9 12 ... 30'''
# num = int(input("Enter a number to print its multiplication table up to 10: ").strip())
# print(f"Multiplication table of {num} is:")
# for i in range(1,11):
#   print(num*i,end=" ")

'''# Input a number n and print its factorial.
# Example: 5 → 120 (because 5×4×3×2×1 = 120)'''
# n = int(input("Enter a number to print its factorial: ").strip())
# fact = 1
# for i in range(1,n+1):
#   fact *= i
# print(fact)

'''# Input a string and count how many vowels are in it.
# Input: "Khan Muhammad" → Output: 4'''
# name = input("Enter your full name: ").strip()
# vowels = "aeiouAEIOU"
# v_c = 0
# for i in name:
#   if i in vowels:
#     v_c += 1
# print(v_c)

'''# Input: 1234 → Output: 1+2+3+4 = 10'''
# n = input("Enter a number: ").strip()
# total = 0 
# for i in n:
#   total += int(i)
# print(total)

'''# Input: 5 → Output:
# *
# **
# ***
# ****
# *****
'''
# for i in range(1,6):
#   print("*"*i)

