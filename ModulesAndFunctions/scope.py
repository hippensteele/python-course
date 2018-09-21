#! /usr/local/bin/python3

__author__="tom"
__date__ ="$Apr 14, 2018 10:14:57 AM$"

def fact(n):
    """ calculate n! iteratively """
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result

def factorial(n):
    """ calculate n! recursively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def fib(n): # slow
    """ F(n) = F(n - 1) + F(n - 2) """
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def fibonacci(n): # faster
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus1 + n_minus2
            n_minus2 = n_minus1
            n_minus1 = result
    return result


for i in range(130):
    print(i, fibonacci(i))