# sum of first N natural numbers


# Functional way
# def sumNos(n):
#     if n==0:
#         return 0
#     return n+sumNos(n-1)

# print(sumNos(5))

# Parameterized way
def sumNos(i, sum):
    if(i<1):
        print(sum)
        return
    sumNos(i-1, sum+i)

sumNos(5, 0)