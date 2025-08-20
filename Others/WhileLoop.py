""""
name = input("Enter your name: ")
while name == "":
    print("You didn't enter name")
    name = input("Enter your name: ")
print(f"Hello {name}")
"""

"""
age = int(input("Enter your age: "))
while age<0:
    print("Age can't be -ve")
    age = int(input("Enter your age: "))
print(f"You are {age} old")
"""

"""
food = input("Enter food you like (q to quit): ")
while not food == "q":
    print(f"you like {food}")
    food = input("Enter another food you like (q to quit): ")

print("bye")
"""

num = int(input("Enter a # b/w 1-10: "))

while num <1 or num > 10:
    print(f"{num} isn't valid.")
    num = int(input("Enter a # b/w 1-10: "))

print(f"your number is {num}")