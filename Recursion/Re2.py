# print name N times using Recursion

def printName(n):
    if n==0:
        return
    print("abc", end=" ")
    printName(n-1)

printName(5)