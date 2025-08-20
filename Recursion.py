'''# 1️⃣ Write a recursive function `sum_n(n)` that returns the sum of first `n` natural numbers.
# For example, sum_n(5) → 15'''
# def sum_n(n):
#     if n ==1:
#       return 1
#     else:
#       return n + sum_n(n-1)
# n = int(input("Enter a number: "))
# print(sum_n(n))

'''# 2️⃣ Write a recursive function `reverse_string(s)` that returns the reverse of the string.
# Example: reverse_string("admin") → "nimda"'''
# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse_string(s[1:]) + s[0]
# print(reverse_string("admin"))

'''# 3️⃣ Write a recursive function `is_palindrome(s)` that checks if a string is a palindrome.
# For example: "madam" → True, "admin" → False'''
# def is_palindrome(s):
#     if len(s) < 1:
#         return True
#     else:
#         if s[0] == s[-1]:
#             return is_palindrome(s[1:-1])
#         else:
#             return False
# print(is_palindrome("madam"))

'''# 4️⃣ Recursively compute the nth Fibonacci number using function `fib(n)`
# Example: fib(6) → 8 (Fibonacci: 0,1,1,2,3,5,8,...)'''
# def fib(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(6))

