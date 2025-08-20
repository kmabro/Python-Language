'''
Create a class `Movie` with attributes `name` and `year`.
Override the __str__ method to return: "Movie: <name> (<year>)"
Create an object and print it.
'''
# class Movie:
#   def __init__(self, name, year):
#     self.name = name
#     self.year = year

#   def __str__(self):
#     return f"Movie: {self.name} ({self.year})"

# obj = Movie("The Matrix", 1999)
# print(str(obj))

'''
Create a class `Point` with attributes `x` and `y`.
Override the __repr__ method to return: "Point(x, y)"
Create and print the object using repr().
'''
# class Point:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y

#   def __repr__(self):
#     return f"Point({self.x}, {self.y})"

# obj = Point(1, 2)
# print(repr(obj))

'''
Create a class `Team` that takes a list of players.
Implement the __len__ method to return the number of players in the team.
Create a team object and print len(team).
'''
# class Team:
#   def __init__(self, players):
#     self.players = players

#   def __len__(self):
#     return len(self.players)
# players_list = ["Khan Muhammad", "xyz", "abc"]
# team = Team(players_list)
# print(len(team))

'''
Create a class `Adder` that stores a number.
Implement the __call__ method so that when you call the object with a value, it adds the stored number and returns the result.
Example: obj = Adder(10); print(obj(5)) → 15
'''
# class Adder:
#   def __init__(self, number):
#     self.number = number

#   def __call__(self, value):
#     return self.number + value

# obj = Adder(10)
# print(obj(5))

'''
Create a class `Rectangle` with `width` and `height`.
Implement __str__ to return: "Rectangle: <width>x<height>"
Also, implement __len__ to return the perimeter of the rectangle.
Create an object and print it, and print its length using len().
'''
# class Rectangle:
#   def __init__(self, width, height):
#     self.width = width
#     self.height = height

#   def __str__(self):
#     return f"Rectangle: {self.width}x{self.height}"

#   def __len__(self):
#     return 2 * (self.width + self.height)

# obj = Rectangle(5, 10)
# print(str(obj))
# print(len(obj))

'''
Create a class `Multiplier` which takes a factor.
Use __call__ to multiply any number passed to the object by this factor.
Then create an object and call it with different numbers.
'''
# class Miltiplier:
#   def __init__(self, factor):
#     self.factor = factor

#   def __call__(self, number):
#     return self.factor * number

# obj = Miltiplier(5)
# print(obj(10))