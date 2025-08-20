
user = input("Enter a username: ")


if len(user) > 12:
    print("can't be more than 12 char: ")
elif not user.find(" ") == -1:
    print("can't contain spaces")
elif not user.isalpha():
    print("can't contain no's ")
else:
    print(f"Welcome {user}")