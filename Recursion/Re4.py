# print N to 1 using Recursion

def printNos(i, n):
    if(i<1):
        return
    print(i, end=" ")
    printNos(i-1, n)

n=5
printNos(n,n)