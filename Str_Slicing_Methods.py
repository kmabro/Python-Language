'''Create a variable name = "Alice" and print: 
Hello, Alice'''
# name = "Alice"
# print("Hello,",name,'\n')
'''Print the following sentence using a string:
He said, "Learning Python is fun!"'''
# print("He said,\"Learning Python is fun!\"",'\n')
# print('He said,"Learning Python is fun!"','\n')
'''Create and print a multi-line string that says:
This is line 1
This is line 2
This is line 3'''
# multi_line_string = """This is line 1
# This is line 2
# This is line 3"""
# print(multi_line_string,'\n')
'''Create a string fruit = "Mango" and print:
The first character
The third character'''
# fruit = "Mango"
# print(fruit[0])
# print(fruit[2],'\n')
'''Write a program that loops through the string "Python" and prints each character on a new line.'''
# str = "Python"
# for i in str:
#   print(i)
'''Use single and double quotes to print:
It's called "Python".'''
# print('\n',"It\'s called \"Python\".")
'''Ask the user to enter a string, and print how many characters it contains.'''
# str = input("Enter a string: ")
# print(len(str))
'''Take a string input from the user and print it in reverse'''
# str = input("Enter a string: ")
# reverse_str = str[::-1]
# print(reverse_str)
'''Create a string word = "Banana" and print:
Banana is a 6 letter word.'''
# word = "Banana"
# print(word,"is a",len(word),"letter word.")
'''Given fruit = "Pineapple", print:
First 4 characters
Last 4 characters
Characters from index 2 to 6'''
# fruit = "Pineapple"
# print(fruit[0:4])
# print(fruit[-4:])
# print(fruit[1:6])

##
##
#String Methods:
##
##
'''Ask the user to enter a string and print it in all uppercase.'''
# str = input("Enter a string: ")
# print(str.upper())
'''Ask the user to enter a string and count how many times the letter "a" appears.'''
# str = input("Enter a string: ")
# print(str.count('a'))
'''Replace all instances of "bad" in the string "This is a bad, really bad day" with "good".'''
# str = "This is a bad, really bad day"
# print(str.replace('bad','good'))
'''Trim extra spaces from the beginning and end of the string " Python is fun! " using .strip().'''
# str = " Python is fun! "
# print(str.strip())
'''Take a sentence from the user and split it into words (print as a list).'''
# str = input("Enter a sentence: ")
# print(str.split())
'''Check if Word Starts with 'S' Ask the user to enter a word'''
# word = input("Enter a word: ")
# print(word.startswith('S'))
'''Ask the user to enter a string and check:

Does it start with "Hello"?

Does it end with "!"?'''
# str = input("Enter a string: ")
# print(str.startswith('Hello'), str.endswith('!'))
'''Input a sentence in lowercase and capitalize it using .capitalize().'''
# str = input("Enter a sentence: ")
# print(str.capitalize())
'''Center the text "Welcome" in a 30-character wide space using "*" as padding.'''
# welcome = "Welcome"
# print(welcome.center(30,'*'))
'''Try to find and index the word "Python" in the string "I love coding in JavaScript".'''
# sen = "I love coding in JavaScript"
# print(sen.find('Python'))
# print(sen.index('Python'))
'''Ask the user to enter a book title and check if it's in title case using .istitle().'''
# title = input("Enter a book title: ")
# print(title.istitle())
'''Given a string, swap its case and count how many characters are now uppercase.'''
# str = "Hello, World!, how are you?"
# print(str.swapcase())
# print(str.swapcase().count('H'))
'''Ask the user to enter a word. Check if it contains only alphabetic characters.'''
# word = input("Enter a word: ")
# print(word.isalpha())
'''Input a string and check if it’s a number. If yes, convert to int and double it.'''
# str = input("Enter a string: ")
# if str.isnumeric():
#     print(int(str)*2)
'''Take a full name input and convert it to title case (first letter of each word capitalized).'''
# name = input("Enter your full name: ")
# print(name.title())
'''Ask the user for a number and display it as a 5-digit number padded with zeros.'''
# num = input("Enter a number: ")
# print(num.zfill(5))
'''Use .partition("is") on the string "Python is fun" and print the 3 parts.'''
# str = "Python is fun"
# print(str.partition("is"))
