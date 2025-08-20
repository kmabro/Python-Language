'''Count from 1 to 10 using a while loop.'''
# count  = 1
# while (count<=10):
#    print(count)
#    count = count + 1

'''Print all even numbers from 10 to 1 using a while loop.'''
# count = 10
# while (count>=1):
#   if count % 2 == 0:
#     print(count)
#   count = count - 1

'''Take a number input from the user and print all numbers from that number down to 1.'''
# num = int(input("Enter a number: "))
# while (num>=1):
#   print(num)
#   num = num - 1
# --  For-version  --
# num = int(input("Enter a number: "))
# for i in range(num, 0, -1):
#   print(i)

'''Create a loop that counts down from 3 to 1 and prints "Go!" using else once done.

Example output:
3
2
1
Go!
'''
# num = 3
# while (num>=1):
#   print(num)
#   num = num - 1
# else:
#   print("Go!")

'''Use a while loop to input numbers from the user until they input 0, then print "Done." using else.'''
# num = int(input("Enter a number: "))
# while num != 0:
#     print(num)
#     num = int(input("Enter a number: "))
# else:
#     print("Done.")

'''Keep asking the user to enter a password until they enter "admin123". Once entered, print "Access Granted!"'''
# while True:
#   password = input("Enter your password: ")
#   if password == "admin123":
#       print("Access Granted!")
#       break

'''Ask the user to enter positive numbers until they enter a non-positive number, then print the total count of numbers they entered.'''
# num = int(input("Enter a positive number: "))
# count = 0
# while num > 0:
#     count += 1
#     num = int(input("Enter a positive number: "))
# print("Total count of numbers entered:", count)

'''Write a loop that keeps adding numbers entered by the user until they type "stop". At the end, print the sum.

Hint: use input() and check for the string "stop".'''
while True:
    num = 