n = int(input("enter n: "))

for i in range(n):
    print("*"*(i+1), " "*(n-i-1))

for i in range(n-1, 0, -1):
    print("*"*(i), " "*(n-i-1))