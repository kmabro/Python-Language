'''
Create a class `Vector2D` with attributes `x` and `y`.
Define the `__init__` method to initialize these attributes.
Create an object and print its x and y values.
'''
# class Vector2D:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y

# obj = Vector2D(5, 10)
# print(obj.x)
# print(obj.y)

'''
Create a class `Vector2D` with attributes `x` and `y`.
Override the `__str__` method so that printing a vector object shows: "Vector with x = <x>, y = <y>"
Create and print a vector object.
'''
# class Vector2D:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y

#   def __str__(self):
#     return f"Vector with x = {self.x}, y = {self.y}"

# obj = Vector2D(5, 10)
# print(obj)

'''
Create a class `Vector2D` with attributes `x` and `y`.
Create two objects of this class.
Manually add the x and y values of both and print the result in the format: "Result x: <value>, y: <value>"
(No operator overloading yet.)
'''
# class Vector2D:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y

# v1 = Vector2D(5, 10)
# v2 = Vector2D(3, 7)

# result_x = v1.x + v2.x
# result_y = v1.y + v2.y

# print(f"Result x: {result_x}, y: {result_y}")

'''
Create a class `Money` with an attribute `amount`.
Override the `__add__` method to add two `Money` objects.
Return a new `Money` object with the total amount.
Create two objects and add them using `+`, then print the result.
'''
# class Money:
#   def __init__(self, amount):
#     self.amount = amount

#   def __add__(self, other):
#     return Money(self.amount + other.amount)

#   def __str__(self):
#     return f"Money amount: {self.amount}"

# am = Money(50)
# am2 = Money(100)
# am3 = am + am2
# print(am3)

'''
Create a class `Temperature` with an attribute `celsius`.
Override the `__sub__` method to subtract temperatures using `-`.
Return a new `Temperature` object.
Print the result of subtracting one temperature from another.
'''
# class Temperature:
#   def __init__(self, celsius):
#     self.celsius = celsius

#   def __sub__(self, other):
#     return Temperature(self.celsius - other.celsius)

#   def __str__(self):
#     return f"Temperature: {self.celsius}C"

# obj1 = Temperature(25)
# obj2 = Temperature(10)
# obj3 = obj1 - obj2
# print(obj3)

'''
Create a class `Vector2D` with attributes `x` and `y`.
Override the `__add__` method to add two vectors.
The result should be a new `Vector2D` object with the sum of x and y values.
Create two vector objects, add them using `+`, and print the result.
'''
# class Vector2D:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y

#   def __add__(self, other):
#     return Vector2D(self.x + other.x, self.y + other.y)

#   def __str__(self):
#     return f"Vector with x = {self.x}, y = {self.y}"

# v1 = Vector2D(5, 10)
# v2 = Vector2D(3, 7)
# v3 = v1+v2
# print(v3)

'''
Create a class `Vector2D` with attributes `x` and `y`.
Override the `__add__` method to add two vectors.
Also override the `__str__` method to display the vector as: "Vector(x, y)"
Create two vectors, add them using `+`, and print the result object.
'''
# class Vector2D:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y

#   def __add__(self, other):
#     return Vector2D(self.x + other.x, self.y + other.y)

#   def __str__(self):
#     return f"Vector({self.x}, {self.y})"

# v1 = Vector2D(5, 10)
# v2 = Vector2D(3, 7)
# v3 = v1 + v2
# print(v3)