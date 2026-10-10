# Recursion using params

'''
Print x, n times
'''

# def func(i, n):
#     if n <= 0:
#         return
#     print(i)
#     func(i, n-1)

# func(10, 5)


'''
Print 1 to N using tail recursion
'''

# def func(i, n):
#     if i > n:
#         return
#     print(i)
#     func(i+1, n)

# func(1, 5)


'''
Print 1 to N using head recursion
'''

# def func(i, n):
#     if i > n:
#         return
#     func(i, n-1)
#     print(n)

# func(1, 5)


'''
Print N to 1 using tail recursion
'''

# def func(i, n):
#     if i > n:
#         return
#     print(n)
#     func(i, n-1)

# func(1, 5)


'''
Print N to 1 using head recursion
'''

# def func(i, n):
#     if i > n:
#         return
#     func(i+1, n)
#     print(i)

# func(1, 5)


'''
Parameterised Recursion
'''

'''
Sum of 1 to N numbers
'''

# def func(sum, i, n):
#     if i > n:
#         print(sum)
#         return
#     sum += i
#     func(sum, i+1, n)

# func(0, 1, 5)

def func(sum, i, n):
    if i > n:
        print(sum)
        return
    func(sum+i, i+1, n)

func(0, 1, 5)