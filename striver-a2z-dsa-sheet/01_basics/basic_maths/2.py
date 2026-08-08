# reverse a number

n = int(input("enter n: "))

r = 0

while n > 0:
    l = n%10
    r = r*10 + l
    n = n//10
    
print(r)