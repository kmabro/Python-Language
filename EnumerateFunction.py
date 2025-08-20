'''# Q1. Use enumerate to print index and value from the list
fruits = ['apple', 'banana', 'cherry']
# Your code here'''
# fruits = ['apple', 'banana', 'cherry']
# for index,value in enumerate(fruits):
#   print(index,value)

'''# Q2. Use enumerate to print index starting from 1 for each item in the list
languages = ['Python', 'Java', 'C++']
# Your code here'''
languages = ['Python', 'Java', 'C++']
# for index,value in enumerate(languages,start=1):
#   print(index,value)

'''# Q3. Use enumerate to print each character and its index in the string
text = "hello"
# Your code here'''
# text = "hello"
# for index,char in enumerate(text):
#   print(index,char)

'''# Q4. Given a list of names, print "Index: Name" using enumerate and f-strings
names = ["Ali", "Sara", "Hamza"]
# Your code here'''
# names = ["Ali", "Sara", "Hamza"]
# for index,name in enumerate(names):
#   print(f"Index: {index} Name: {name}")

'''# Q5. Use enumerate to find the index of the first word that starts with "b"
words = ['apple', 'banana', 'cherry', 'blueberry']
# Your code here'''
# words = ['apple', 'banana', 'cherry', 'blueberry']
# for index,word in enumerate(words):
#   if word.startswith('b'):
#     print(index)

'''# Q6. Given a tuple of colors, print only the elements at even indices using enumerate
colors = ('red', 'green', 'blue', 'yellow')
# Your code here'''
# colors = ('red', 'green', 'blue', 'yellow')
# for index,color in enumerate(colors):
#   if index % 2 == 0:
#     print(color)

'''# Q7. Write a program that adds up the values at even indexes in a list
nums = [5, 10, 15, 20, 25]
# Expected: 5 (index 0) + 15 (index 2) + 25 (index 4) = 45
# Your code here'''
# nums = [5, 10, 15, 20, 25]
# sum_even = 0
# for index, num in enumerate(nums):
#     if index % 2 == 0:
#         sum_even += num
# print(sum_even)

'''# Q8. Reverse a string using a loop and enumerate (do NOT use slicing or reversed())
word = "python"
# Your code here'''
# word = "python"
# for index,char in enumerate(word):
#   print(word[len(word)-index-1])

'''# Q9. Count how many vowels are present at even indices in a string using enumerate
s = "enumerate"
# Your code here'''
s = "enumerate"
# count = 0
# vowels = 'aeiou'

# for index, char in enumerate(s):
#     if index % 2 == 0 and char.lower() in vowels:
#         count += 1

# print("Vowels at even indices:", count)
