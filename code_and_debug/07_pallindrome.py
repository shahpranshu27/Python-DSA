# Pallindrome

num = 123
num1 = num
rev = 0
while num > 0:
    n = num % 10
    rev = rev*10 + n
    num = num // 10

print(rev)
print(num1)
print(rev == num1)