# print 1 to N using Recursion

def printNos(i, n):
    if i>n:
        return
    print(i, end=" ")
    printNos(i+1, n)

printNos(1, 5)