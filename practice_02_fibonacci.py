n = int(input("Enter fibonacci numbers: "))
ans = []

a, b = 0, 1
ans.append(a)

for i in range(1, n):
    ans.append(b)
    c = a + b
    a = b
    b = c
print(ans)