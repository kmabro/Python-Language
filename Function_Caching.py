'''___
Write a function `factorial(n)` that calculates the factorial of a number `n`.
Use `@functools.lru_cache` to cache results.
Test it by calling factorial(10) and factorial(5).
___'''
# import functools
# @functools.lru_cache(maxsize=None)
# def factorial(n):
#   if n == 0:
#     return 1
#   else:
#     return n * factorial(n-1)
# fact = factorial(10)
# print(fact)

'''___
Modify the Fibonacci function to use `lru_cache` and print the 30th Fibonacci number.
Also, print how many times the function was called using the `fib.cache_info()` method.
___'''
# import functools
# @functools.lru_cache(maxsize=None)
# def fib(n):
#   if n < 2:
#     return n
#   else:
#     return fib(n-1) + fib(n-2)

# Fib = fib(30)
# print(Fib)
# print(fib.cache_info())

'''___
Write a recursive function `power(base, exp)` that computes base raised to exp.
Use `lru_cache` to speed up repeated calls and test it with `power(2, 10)` and `power(2, 15)`.
___'''
# import functools
# @functools.lru_cache(maxsize=None)
# def power(base, exp):
#     if exp == 0:
#         return 1
#     elif exp == 1:
#         return base
#     else:
#         return base * power(base, exp - 1) 

# p1 = power(2, 10)
# p2 = power(2, 15)
# print(p1)  
# print(p2)  
# print(power.cache_info()) 

