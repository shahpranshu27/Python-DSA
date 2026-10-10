# Recursion using Function >> Functional Recursion

'''
Sum of 1 to N using Functional Recursion
'''

def func(n):
    if n == 1:
        return 1
    
    return n + func(n-1)

print(func(5))