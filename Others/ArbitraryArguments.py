"""
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3,4,5))
"""

"""
def d(*args):
    for arg in args:
        print(arg, end=" ")
d("Khan","Muhammad")
"""

"""
def a(**kwargs):
    for key in kwargs.values():
        print(key)

print(a(street= "123 Fake Street",
        city="Detroit",
        state ="MI",
        zip="54321" , ))
"""

def s(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")


s("Dr.", "Khan", "M", "Abro",
  street = "123 ",
  apt = "10",
  city = "Suk.",
  country = "Pak")

