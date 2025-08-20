#**************************#
#***** Metacharacters *****#
#**************************#
''' []	A set of characters'''
# import re
# txt = "I am Khan Muhammad"
# x = re.findall("[a-m]", txt)
# print(x)
''' \	 Signals a special sequence (can also be used to escape special characters)'''
# import re
# txt = "My Id is: 133-23-0037"
#Find all digit characters:
# x = re.findall("\d", txt)
# print(x)
''' .	 Any character (except newline character)'''
# import re
# txt = "what Nail Hell Sell Jell"
# x = re.findall("..ll", txt)
# print(x)
''' ^	 Starts with'''
# import re
# txt = "Who are you? can you tell me?"
# x = re.findall("^Who", txt)
# if x:
#   print("Yes, the string starts with 'Who'")
# else:
#   print("No match")
''' $ 	Ends with'''
# import re
# txt = "Who are you? can you tell me."
# x = re.findall("me.$", txt)
# if x:
#   print("Yes, the string ends with 'me.'")
# else:
#   print("No march")
''' *	Zero or more occurrences'''
# import re
# txt = "The rain in Spain falls mainly in the plain!"
# x = re.findall("ain*", txt)
# print(x)
''' +	One or more occurrences'''
# import re
# txt = "The rain in Spain falls mainly in the plain!"
# x = re.findall("ai+", txt)
# print(x)
''' ?	Zero or one occurrences'''
# import re
# txt = "Hello world, i am learning Python."
# x = re.findall("o?", txt)
# print(x)
''' {}	Exactly the specified number of occurrences'''
# import re
# txt = "The rain in Spain falls mainly in the plain!"
# x = re.findall("a{1}.n", txt)
# print(x)
''' |	Either or'''
# import re
# txt = "Hello world, i am learning Python."
# x = re.findall("Python|stays", txt)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

#*****************#
#***** Flags *****#
#*****************#
''' re.ASCII	re.A	Returns only ASCII matches'''
# import re
# txt = "Hello world, i am learning Python."
# x = re.findall(r"\w",txt, re.ASCII)
# print(x)
''' re.DEBUG		Returns debug information'''
# import re
# txt = "Hello world, i am learning Python."
# x = re.findall(r"\w",txt, re.DEBUG)
# print(x)
''' re.DOTALL	re.S	Makes the . character match all characters (including newline character)'''
# import re
# txt = '''Hello
# world,
# i am
# learning
# Python.'''
# x = re.findall("am.learning",txt, re.DOTALL)
# print(x)
''' re.IGNORECASE	re.I	Case-insensitive matching'''
# import re
# txt = "Hello world, i am learning Python and i am enjoying it."
# x = re.findall("Am",txt, re.IGNORECASE)
# print(x)
''' re.MULTILINE	re.M	Returns only matches at the beginning of each line'''
# import re
# txt = """There
# aint much
# rain in
# Spain"""
# x = re.findall("^ain",txt, re.MULTILINE)
# print(x)
''' re.NOFLAG		Specifies that no flag is set for this pattern'''
# import re
# txt = "Python is python and PYTHON."
# x = re.findall(r"Python", txt, re.NOFLAG)
# print(x)
''' re.UNICODE	re.U	Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches'''
# import re
# txt = "Hello world, i am learning Python."
# x = re.findall(r"\w",txt, re.UNICODE)
# print(x)
'''re.VERBOSE	re.X	Allows whitespaces and comments inside patterns. Makes the pattern more readable'''
# import re
# txt = "Hello world, i am learning Python."
# x = re.findall(r"Python", txt, re.VERBOSE)
# print(x)

#*****************************#
#***** Special Sequences *****#
#*****************************#
''' \A	Returns a match if the specified characters are at the beginning of the string'''
# import re
# txt = "Hello world, i am learning Python."
# x = re.findall("\AHello", txt)
# print(x)
# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")
''' \b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")'''
# import re
# txt = "Hello world, i am learning Python."
# x = re.findall(r"\bPytho", txt)
# print(x)
# y = re.findall(r"ython\b", txt)
# print(y)
''' \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")'''
# import re
# txt = "Hello world, i am learning Python."
# x = re.findall(r"\Bearning", txt)
# print(x)
# y = re.findall(r"world\B", txt)
# print(y)
''' \d	Returns a match where the string contains digits (numbers from 0-9)'''
# import re
# txt = "my Id is: 133-23-0037"
# print(re.findall("\d", txt))
''' \D	Returns a match where the string DOES NOT contain digits'''
# import re
# txt = "my Id is: 133-23-0037"
# print(re.findall("\D", txt))
''' \s	Returns a match where the string contains a white space character'''
# import re
# txt = "Hello world, i am learning Python."
# print(re.findall("\s", txt))
''' \S	Returns a match where the string DOES NOT contain a white space character'''
# import re
# txt = "Hello world, i am learning Python."
# print(re.findall("\S", txt))
''' \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)'''
# import re
# txt = "Hello world, i am learning Python and i'd is 133-23-0037."
# print(re.findall("\w", txt))
''' \W	Returns a match where the string DOES NOT contain any word characters'''
# import re
# txt = "my I'd is: 133-23-0037"
# print(re.findall("\W", txt))
''' \Z	Returns a match if the specified characters are at the end of the string'''
# import re
# txt = "I am learning Python."
# print(re.findall("Python.\Z", txt))

#****************#
#***** Sets *****#
#****************#

#import re
''' [arn]	Returns a match where one of the specified characters (a, r, or n) is present'''
# txt = "I am learning Python."
# print(re.findall("[arn]", txt))
''' [a-n]	Returns a match for any lower case character, alphabetically between a and n'''
# txt = "I am learning Python."
# print(re.findall("[a-n]", txt))
''' [^arn]	Returns a match for any character EXCEPT a, r, and n'''
# txt = "I am learning Python."
# print(re.findall("[^arn]", txt))
''' [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present'''
# txt = "My I'd is: 133-23-0037"
# print(re.findall("[0123]", txt))
''' [0-9]	Returns a match for any digit between 0 and 9'''
# txt = "My I'd is: 133-23-0037 and score in DLD was 97"
# print(re.findall("[0-9]", txt))
''' [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59'''
# txt = "My I'd is: 133-23-0037 and score in DLD was 97"
# print(re.findall("[0-5][0-9]", txt))
''' [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case'''
# txt = "I am learning Python."
# print(re.findall("[a-zA-Z]", txt))
''' [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string'''
# txt = "I am learning Python and i am enjoying it."
# print(re.findall("[+]", txt))
# print(re.findall(".", txt))
''' The findall() Function'''
# import re
# txt = "I am learning Python and i am enjoying it."
# print(re.findall("am", txt))
# print(re.findall("who", txt))
''' The search() Function'''
# import re
# txt = "I am learning Python and i am enjoying it."
# x = re.search("Don't", txt)
# print(x)
# y = re.search("\s", txt)
# print("The first white-space character is located in position:", y.start())
''' The split() Function'''
# import re
# txt = "I am learning Python and i am enjoying it."
# x = re.split("\s", txt)
# print(x)
# y = re.split("\s", txt, 1)
# print(y)
''' The sub() Function'''
# import re
# txt = "I am learning Python and i am enjoying it."
# x = re.sub("\s", "-", txt)
# print(x)
# y = re.sub("\s", "-", txt, 2)
# print(y)
''' Match Object'''
# import re
# txt = "The rain in Spain"
# x = re.search("ai", txt)
# print(x)
# y = re.search(r"\bS\w+", txt)
# print(y.span())
# z = re.search(r"\bS\w+", txt)
# print(z.string)
# a = re.search(r"\bS\w+", txt)
# print(a.group())
'''___
Write a program that checks if the word "hello" exists in a given string using `re.search()`.
If found, print "Found!" otherwise "Not Found".
Test it with: "Say hello to the world".
___'''
# import re
# str = "Say hello to the world"
# if re.search(r"hello", str):
#   print("Found!")
# else:
#   print("Not Found")
'''___
Extract all the words ending with "at" from the string "The cat sat on the mat with a hat" using `re.findall()`.
___'''
# import re
# str = "The cat sat on the mat with a hat"
# print(re.findall(r"[a-z]+at", str))
'''___
Replace all words that end with "at" in the string "The cat sat on the mat" with "dog" using `re.sub()`.
___'''
# import re
# str = "The cat sat on the mat"
# print(re.sub(r"[a-z]+at", "dog", str))
'''___
From the string "Contact me at abc123@gmail.com or test.email@yahoo.com", extract all email addresses using regular expressions.
___'''
# import re
# str = "Contact me at abc123@gmail.com or test.email@yahoo.com"
# emails = re.findall(r'\S+@\S+', str)
# print("Found emails:", emails)
'''___
Write a regex to find all 3-letter lowercase words in the sentence: "The fox ran to the hut and saw a bat".
Use `re.findall()` and print the result.
___'''
# import re
# sent = "The fox ran to the hut and saw a bat"
# print(re.findall(r"\b[a-z]{3}\b", sent))
''' Write a function that takes a string and returns True if it’s a valid email address, else False.'''
# import re
# def is_valid_email(email):
#   x = re.search("^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$", email)
#   if x:
#     return True
#   else:
#     return False

# print(is_valid_email("kmabro786110@gmail.com"))
# print(is_valid_email("kmabro786110gmail.com"))
'''Given an HTML string, extract all URLs (href links).'''
# import re
# def extract_urls(html):
#   return re.findall(r'href=["\'](https?://[^"\']+)["\']', html)

# print(extract_urls('<a href="https://www.example.com">Example</a>'))
# print(extract_urls('<a href="https://www.example.com">Example</a> <a href="https://www.example2.com">Example2</a>'))
'''Extract all hashtags from a given tweet.'''
# import re
# def hashtags(tweet):
#   return re.findall(r'#\w+', tweet)

# print(hashtags('I am learning Python and i am enjoying it. #Python #Learning #Python3'))
'''Validate if a string is a valid IPv4 address.'''
# import re
# def is_valid_ipv4(ip):
#   return bool(re.match(r'^(\d{1,3}\.){3}\d{1,3}$', ip))

# print(is_valid_ipv4('192.168.1.1'))
# print(is_valid_ipv4('192.168.1.1.1'))
