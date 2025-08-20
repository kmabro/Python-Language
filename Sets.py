'''# 1️⃣ Create a set with the elements "apple", "banana", and "cherry". Print the set.'''
# fruits = {"apple", "banana", "cherry"}
# print(fruits)

'''# 2️⃣ Try creating an empty set and print its type to confirm it's a set.'''
# empty_set = set()
# print(type(empty_set))

'''# 3️⃣ Add the element "orange" to the set `fruits`. Print the updated set.'''
# fruits = {"apple", "banana", "cherry"}
# fruits.add("orange")
# print(fruits)

'''# 4️⃣ Use a for loop to print all elements in the set `colors`.'''
# colors = {"red", "green", "blue"}
# for color in colors:
#   print(color)

# 5️⃣ Try to add a duplicate element "apple" into the `fruits` set and observe the result.
# fruits = {"apple", "banana", "cherry"}
# fruits.add("apple") ## Should not add again
# print(fruits)

'''# 6️⃣ Check if "banana" is present in the set `fruits`.
fruits = {"apple", "banana", "cherry"}'''
# fruits = {"apple", "banana", "cherry"}
# if "banana" in fruits:
#   print("banana is present in the set")
# else:
#   print("banana is not present in the set") 


##### SET METHODS #####
'''# 1️⃣ Create two sets `A` and `B`. Use `union()` to create a third set `C` that contains all unique elements from both sets. Print C.'''
# A = {1, 2, 3}
# B = {3, 4, 5}
# C = A.union(B)
# print(C)

'''# 2️⃣ Create two sets `A` and `B`. Update set `A` to include elements from set `B` using the `update()` method. Print A.'''
# A = {1, 2, 3}
# B = {3, 4, 5}
# A.update(B)
# print(A)

'''# 3️⃣ Create two sets with some common elements. Use `intersection()` to create a third set that contains only common elements. Print the result.'''
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# C = A.intersection(B)
# print(C)

'''# 4️⃣ Use `intersection_update()` to keep only common elements in a set. Print the updated set.'''
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# A.intersection_update(B)
# print(A)

'''# 5️⃣ Create two sets and use `symmetric_difference()` to find elements not common to both sets. Print the result.'''
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# C = A.symmetric_difference(B)
# print(C)

'''# 6️⃣ Use `symmetric_difference_update()` on a set with another. Print the final result.'''
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# A.symmetric_difference_update(B)
# print(A)

'''# 7️⃣ Use `difference()` to find which elements are in set A but not in set B. Print the result.'''
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# C = A.difference(B)
# print(C)

'''# 8️⃣ Use `difference_update()` to remove elements from A that are also in B. Print the updated set.'''
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# A.difference_update(B)
# print(A)

'''# 9️⃣ Create two sets and check if they are disjoint using `isdisjoint()`. Print the result.'''
# A = {1, 2, 3, 4}
# B = {5, 6, 7, 8}
# C = A.isdisjoint(B)
# print(C)

'''# 🔟 Create a set and check if it is a superset of another set using `issuperset()`. Print the result.'''
# A = {1, 2, 3, 4, 5, 6}
# B = {3, 4, 5}
# C = A.issuperset(B)
# print(C)

'''# 1️⃣1️⃣ Create a set and check if it is a subset of another set using `issubset()`. Print the result.'''
# A = {1, 2, 3, 4, 5, 6}
# B = {3, 4, 5}
# C = B.issubset(A)
# print(C)

'''# 1️⃣2️⃣ Create a set and use `add()` to insert one new element. Print the updated set.'''
# A = {1, 2, 3, 4, 5, 6}
# A.add(7)
# print(A)

'''# 1️⃣3️⃣ Use `update()` to add multiple items (as a list or another set) to a set. Print the updated set.'''
# A = {1, 2, 3, 4, 5, 6}
# B = {7, 8, 9, 10}
# C = (11, 12, 13)
# A.update(B)
# print(A)
# A.update(C)
# print(A)

'''# 1️⃣4️⃣ Use `remove()` to delete an existing item from a set. Print the result.'''
# A = {1, 2, 3, 4, 5, 6}
# A.remove(3)
# print(A)

'''# 1️⃣5️⃣ Try using `remove()` on a non-existing item and observe what error you get.'''
# A = {1, 2, 3, 4, 5, 6}
# A.remove(7)
# print(A)    

'''# 1️⃣6️⃣ Use `discard()` to delete an item from a set. Try discarding an item that doesn’t exist. Print result.'''
# A = {1, 2, 3, 4, 5, 6}
# A.discard(6)
# print(A)
# A.discard(7) # No error
# print(A)

'''# 1️⃣7️⃣ Create a set and use `pop()` to remove an item. Print both the item removed and the updated set.'''
# A = {1, 2, 3, 4, 5, 6}
# A.pop()
# print(A)

'''# 1️⃣8️⃣ Use `clear()` to empty a set. Print it afterwards.'''
# A = {1, 2, 3, 4, 5}
# A.clear()
# print(A)

'''# 1️⃣9️⃣ Use `del` to delete an entire set. Try printing it after deletion to confirm it's removed.'''
# A = {1, 2, 3, 4, 5}
# del A
# print(A)  #NameError: name 'A' is not defined

'''# 2️⃣0️⃣ Create a set and use an `if` statement to check if a certain item exists. Print a message based on presence.'''
# A = {1,2,3,4,5}
# if 3 in A:
#   print("3 is present in the set")
# else:
#   print("3 is not present in the set")
