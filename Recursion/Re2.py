# print name N times using Recursion

def printName(n):
    if n==0:
        return
    printName(n-1)
    print("abc", end=" ")

printName(5)