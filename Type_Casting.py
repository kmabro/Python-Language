a = '1'
b = '2'

print(a + b)
print(int(a) + int(b))  #Typecasting
'''Convert the string "100" to an integer and add 25 to it. Print the result.'''
c = '100'
d = 25
print('\n', int(c) + d, '\n')
'''Convert 9.87 to an integer and print the result and its type.'''
e = 9.87
print(int(e), type(int(e)), '\n')
'''Convert the string "45.67" to a float and multiply it by 2. Print the result.'''
f = "45.67"
print(float(f) * 2, '\n')
'''Try to add a string "50" and an integer 10 without converting. What happens? Then fix it using explicit typecasting.'''
g = "50"
h = 10
# print(g+h,'\n') --> TypeError: can only concatenate str (not "int") to str
print(int(g) + h, '\n')
'''Convert the number 255 to hexadecimal and octal using hex() and oct(). Print both results.'''
i = 255
print(hex(i), oct(i), '\n')
'''Add an integer 10 and a float 2.5. Print the result and the data type.'''
j = 10
k = 2.5
print(j + k, type(j + k), '\n')
'''Use ord() to get the ASCII value of the character 'A' and print it.'''
l = 'A'
print(ord(l), '\n')
'''Convert the tuple (1, 2, 3) to a list using list() and print it.'''
m = (1, 2, 3)
print(m, '\n')
print(list(m), '\n')
'''Convert the set {5, 10, 15} to a list and print the type.'''
n = {5, 10, 15}
print(n, '\n')
print(list(n), type(list(n)), '\n')
'''Convert the string "Python" to a list of characters and print the list.'''
o = "Python"
print(list(o), '\n')
