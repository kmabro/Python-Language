"""
def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello(last="M", greeting= "Hello", title = "Mr.", first="Khan" )
"""

"""
for x in range(1,11):
    print(x, end = " ")
"""

def get_phone(c,a,f,l):
    return f"{c}-{a}-{f}-{l}"

phone_num = get_phone(c = 1, a= 123, f= 456, l= 7890)

print(phone_num)