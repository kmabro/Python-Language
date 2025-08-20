"""
def prices(price, discount = 0, tax = 0.05):
    return price * (1- discount) * (1 + tax)

#print(prices(500,0,0.05))
print(prices(500,0.1, 0))
"""

import  time

def count(start,end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(0,10)