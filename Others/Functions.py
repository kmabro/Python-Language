"""
def hb(name,age):
      print("Hi")
      print("Hello")
      print(f"How are you {name}")
      print(f"You are {age} years old")

hb("Khan",20)
"""

"""
def di(name,amount,date):
      print(f"Hello {name}")
      print(f"your bill of {amount:.2f} is due: {date}")

di("Khan", 400,20)
"""

"""
def add(x,y):
      z = x+y
      return z
def sub(x,y):
      z = x-y
      return z
def mul(x,y):
      z = x*y
      return z
def div(x,y):
      z = x/y
      return z

print(add(10,10))
print(sub(10,10))
print(mul(10,10))
print(div(10,10))
"""

def name(first,last):
      first = first.capitalize()
      last = last.capitalize()
      return first +" " +last

full_name = name("khan ", "muhammad")
print(full_name)