'''1. Predict the output:

a = [10, 20]
b = [10, 20]
print(a == b)
print(a is b)
'''
# a = [10, 20]
# b = [10, 20]
# print(a == b)
# print(a is b)
# print(id(a)) # Shows memory address of object a
# print(id(b)) # Shows memory address of object b

'''2. Predict the output:

x = "python"
y = "python"
print(x == y)
print(x is y)
'''
# x = "python"
# y = "python"
# print(x == y)
# print(x is y)

'''3. Create two different dictionary objects with the same key-value pairs. Use `==` and `is` to show the difference in their behavior.'''
# dic1 = {'a': 1, 'b': 2, 'c': 3}
# dic2 = {'a': 1, 'b': 2, 'c': 3}
# print(dic1 == dic2)
# print(dic1 is dic2)

'''4. Write a function `compare_objects(a, b)` that returns:
- "Same object" if a is b
- "Equal value" if a == b but not the same object
- "Different" otherwise
Test it with integers, strings, and lists.'''
# def compare_objects(a, b):
#     if a is b:
#         return "Same object"
#     elif a == b:
#         return "Equal value"
#     else:
#         return "Different"

# print(compare_objects(1, 1))

'''5. Predict the output:

a = 256
b = 256
print(a == b)
print(a is b)

a = 300
b = 300
print(a == b)
print(a is b)
'''
# Hint: Python caches small integers.
# a = 256
# b = 256
# print(a == b)
# print(a is b)

# a = 300
# b = 300
# print(a == b)
# print(a is b)

'''6. True or False? The statement `(x is not y)` always means `(x != y)`. Explain with a code example.'''
# x = [1, 2, 3]
# y = [1, 2, 3]
# print(x is not y) # True

