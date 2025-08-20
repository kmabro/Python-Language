# a = True
# print(a := False)

'''___
Ask the user to enter numbers repeatedly.
Stop when the number entered is greater than 100.
Use the Walrus Operator to store the user input and check the condition in a single line.
___'''
# nums = []
# while (num := int(input("Enter a number: "))) <= 100:
#   nums.append(num)
# print(nums)

'''___
Create an empty list called `names`.
Ask the user to enter names until they type "stop".
Use the Walrus Operator to simplify the while loop.
Append each name to the list and print the final list at the end.
___'''
# names = []
# while (name := input("Enter a name: ")) != "stop":
#     names.append(name) 
# print(names)

'''___
Ask the user to enter integers until they type "end".
Use the Walrus Operator to get input and check if the value is an even number.
Store only even numbers in a list and print the list at the end.
(Hint: Use int() conversion inside the walrus operator)
___'''
# nums = []
# while (num := input("Enter an integer:")) != "end":
#     if int(num) % 2 == 0:
#         nums.append(int(num))
# print(nums)

'''___
Ask the user to input words.
Continue asking until they enter an empty string.
Use the Walrus Operator inside the while loop to collect and immediately print the word in reverse.
___'''
# while (word := input("Enter a word: ")) != "":
#   reversed_word = word[::-1]  
#   print(reversed_word)  

'''___
Use the Walrus Operator in a while loop to ask the user for numbers.
Keep adding them to a sum **only if they are positive**.
Stop when a non-positive number is entered and print the total sum.
___'''
# sum = 0
# while (num := int(input("Enter a number: "))) > 0:
#   sum += num
# print(sum)