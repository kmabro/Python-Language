# Exercise 2 Shopping Cart Program
# Iteam, price and quantity

item = input("what item you want purchase ")
price = float(input("what is the price "))
quantity = int(input("How many items "))
total = price * quantity

print(f"You have bought {item} ")
print(f"price of each is {price }")
print(f"You have purchased {quantity } items")
print(f"Total price is R.S:{total}")