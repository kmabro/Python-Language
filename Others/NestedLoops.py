

r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

s = input("Enter a Symbol to use: ")

for x in range(r):
    for y in range(c):
        print(s,end=" ")
    print()