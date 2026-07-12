n = int(input("enter n: "))

for i in range(0, n):
    print((n-i-1)*" ", (2*i+1)*"*", (n-i-1)*" ")