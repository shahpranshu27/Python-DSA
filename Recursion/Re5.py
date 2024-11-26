# sum of first N natural numbers


# Functional way
# def sumNos(n):
#     if n==0:
#         return 0
#     return n+sumNos(n-1) # n + f(n-1)

'''
example: f(3) -> 3 + f(2)
         f(2) -> 2 + f(1)
         f(1) -> 1 + f(0)
         f(0) -> 0
'''

# print(sumNos(5))

# Parameterized way
def sumNos(i, sum):
    if(i<1):
        print(sum)
        return
    sumNos(i-1, sum+i)

sumNos(5, 0)