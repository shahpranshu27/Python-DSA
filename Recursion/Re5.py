# sum of first N natural numbers

def sumNos(n):
    if n==0:
        return 0
    return n+sumNos(n-1)

print(sumNos(5))