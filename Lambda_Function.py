'''1. Create a lambda function that takes one argument and returns its square.'''
# square = lambda x: x ** 2
# print(square(5))

'''2. Use a lambda function to find the cube of a number provided by the user.'''
# cube = lambda x: x*x*x
# print(cube(5))

'''3. Define a lambda function that returns the larger of two numbers.'''
# larger = lambda x,y: x if x>y else y
# print(larger(5,6))

'''4. Create a lambda function that adds three numbers. Call it with values (2, 4, 6).'''
# add_3_nums = lambda x,y,z: x+y+z
# print(add_3_nums(2,4,6))

'''5. Create a lambda function that takes three numbers and returns the maximum among them.'''
# larger_3 = lambda x,y,z: x if x>y and x>z else y if y>z else z
# print(larger_3(2,4,6))

'''1. Use the `map()` function with a lambda to convert a list of temperatures in Celsius to Fahrenheit. Use the formula F = (C * 9/5) + 32.'''
# celsius_temps = [0, 20, 25, 30, 37, 100]
# fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
# print(f"Celsius: {celsius_temps}")
# print(f"Fahrenheit: {fahrenheit_temps}")

'''2. Given a list of strings, use `map()` and a lambda function to convert each string to uppercase.'''
# Strs = ["hello", "world", "python", "programming"]
# uppercase_strs = list(map(lambda str: str.upper(), Strs))
# print(uppercase_strs)

'''3. Use `map()` and a lambda function to find the length of each string in a list of strings.'''
# Strs = ["hello", "world", "python", "programming"]
# lengths = list(map(lambda str: len(str), Strs))
# print(Strs)
# print(lengths)

'''4. Given a list of integers, use `filter()` to keep only the numbers that are divisible by 3.'''
# ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nums_3 = list(filter(lambda x: x%3==0, ints))
# print(ints)
# print(nums_3)

'''5. From a list of words, use `filter()` with a lambda function to return only those words which start with the letter 's' or 'S'.'''
# words = ["hello", "world", "python", "programming", "science", "Solar"]
# starts_with_s = list(filter(lambda word: word[0]=='s' or word[0]=='S', words))
# print(words)
# print(starts_with_s)

'''6. Use `filter()` and a lambda to extract all elements from a list of numbers that are perfect squares. (Hint: Use x**0.5 to get square root, then check if it's int).'''
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 16, 25, 36, 49, 64, 81, 100]
# sqrs = list(filter(lambda x: x**0.5==int(x**0.5), nums))
# print(nums)
# print(sqrs)

'''7. Use `reduce()` from the `functools` module and a lambda to find the product of all elements in a list.'''
# from functools import reduce
# L = [1, 2, 3, 4, 5]
# L_P = reduce(lambda x,y: x*y, L)
# print(L_P)

# '''8. Use `reduce()` and a lambda to find the maximum element in a list of numbers.'''
# from functools import reduce
# L = [1, 2, 3, 4, 5]
# L_M = reduce(lambda x,y: x if x>y else y, L)
# print(L_M)

'''9. Combine `map()` and `filter()` in a single line to square all even numbers in a list.'''
# L = [1,2,3,4,5,6,7,8,9,10]
# S = list(map(lambda x: x*x, filter(lambda x: x%2==0, L)))
# print(S)