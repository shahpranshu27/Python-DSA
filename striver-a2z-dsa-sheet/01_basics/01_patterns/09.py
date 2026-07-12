n = int(input("enter n: "))


for i in range(0, n):
    print((n-i-1)*" ", (2*i+1)*"*", (n-i-1)*" ")
    
for i in range(n, 0, -1):
    print(" "*(n-i), "*"*(2*i-1), " "*(n-i))