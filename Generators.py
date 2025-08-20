'''___
Write a generator function `count_up_to(n)` that yields numbers from 1 to `n`.
Use a for loop to print all values yielded by the generator for n = 5.
___'''
# def count_up_to(n):
#   for i in range(1, n+1):
#     yield i

# gen = count_up_to(5)
# for i in gen:
#   print(i)

'''___
Create a generator function `even_numbers(limit)` that yields only even numbers up to the given `limit`.
Test it with limit = 10.
___'''
# def even_numbers(limit):
#   for i in range(2, limit+1, 2):
#     yield i

# gen = even_numbers(10)
# for i in gen:
#   print(i)

'''___
Write a generator expression that generates the square of numbers from 1 to 10.
Use a for loop to print each value.
___'''
# def square_numbers():
#   for i in range(1, 11):
#     yield i**2

# gen = square_numbers()
# for i in gen:
#   print(i)

'''___
Write a generator function `reverse_string(s)` that yields characters of string `s` in reverse order.
Use it to reverse the string "hello".
___'''
# def reverse_string(s):
#   for i in range(len(s)-1, -1, -1):
#     yield s[i]

# gen = reverse_string("hello")
# print("".join(gen))