# Recursion using params

'''
Print x, n times
'''

def func(i, n):
    if n <= 0:
        return
    print(i)
    func(i, n-1)

func(10, 5)