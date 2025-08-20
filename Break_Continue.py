'''# Write a loop that prints numbers from 1 to 10.
# Stop the loop when the number 7 is encountered.'''
# for i in range(1, 11):
#   if i == 7:
#     break
#   print(i)

'''# Ask the user to guess a secret word.
# Keep asking until they enter "python", then break and print "Correct!".'''
# word = input("Guess the secret word: ")
# while True:
#   if word == "python" or word == "Python":
#     print("Correct!")
#     break
#   word = input("Guess the secret word: ")

'''# Loop through numbers from 1 to 100.
# Print the first number that is divisible by 13 and break the loop.'''
# for i in range(1, 101):
#   if i % 13 == 0:
#     print(i)
#     break

'''# Print numbers from 1 to 20, skipping numbers that are divisible by 3.'''
# for i in range(1, 21):
#   if i%3 == 0:
#     continue
#   print(i)

'''# Loop through each letter in a user-input string.
# Print only the vowels using continue.'''
# str = input("Enter a string: ").strip().lower()
# for i in str:
#     if i not in "aeiou":
#         continue
#     print(i, end=" ")

'''# Loop from 1 to 10.
# Print the square of only even numbers using continue.'''
# for i in range(1, 11):
#     if i%2 != 0:
#         continue
#     print(i**2)

'''# Take 10 numbers from user input one by one.
# Skip (continue) if the number is 0.
# Stop (break) if the number is negative.
# Otherwise, print the number.'''
# for i in range(10):
#     num = int(input("Enter a number: "))
#     if num == 0:
#         continue
#     elif num < 0:
#         break
#     print(num)