
from types import TracebackType


a = 1
print(a)
b= "Khan Muhammad\n"
print(b)

#can't do: print(a+b), will give error 

a = 2
c = 4
print(a+c)

print()
print(type(b)) # b= "Khan Muhammad\n"
print("Type of a is",type(a)) # a = 2

d = True
e = 5.1
f = complex(2,3)
print(type(d))
print(type(e))
print(type(f))

g = None
print(type(g))

'''Create the following variables and assign them values:

An integer variable age with value 25

A float variable height with value 5.8

A string variable name with value "Alice"

A boolean variable is_student with value True'''

age = 25
height = 5.8
name = "Alice"
is_student = True

print("\n","age:",age,"height:",height,"name:",name,"Studnet:",is_student)

'''For the variables you created above, print the data type of each using the type() function.'''
print("\n")
print(type(age))
print(type(height))
print(type(name))
print(type(is_student))
print("\n")

x = "5"
y = 5
print(type(x))
print(type(y))
print("\n")

'''Create a variable z with value 3 + 4j (complex number) and print its type and value.
'''

z= complex(3,4)
print(type(z))

'''Assign values to a = 10, b = 20.5, c = "Python" in one line and print all three.'''

a,b,c = 10,20.5,"Python"
print("\n",a,b,c,"\n")


'''Create a variable named value and assign it None. Print its type.'''
value = None
print("\n",type(value),"\n")

'''Create a variable counter with value 10. Add 5 to it and print the updated value.'''
counter = 10
counter = counter + 5
#counter += 5
print(counter,"\n")

'''Create two variables: first_name = "John" and last_name = "Doe". Combine them into a full name and print it like:
Full Name: John Doe
'''
first_name = "John"
last_name = "Doe"
print("\n","Full Name:",first_name,last_name,"\n")

'''Write a program that compares two numbers and stores the result (True/False) in a boolean variable. Then print it.'''
num1 = 10
num2 = 20
result = num1 == num2
print(result,"\n")

'''Convert a float value 5.9 to integer and print it along with its type.'''
number = 5.9
updated_number = int(number)
print(updated_number,type(updated_number))



