'''
Fibonacci using Recursion
'''

def func(n):
    if n <= 1:
        return 1
    return func(n-1) + func(n-2)

print(func(8))