# 3,2,5,8,9,10,11

nums = list(map(int, input().split(',')))
fib_set = set()

a, b = 1, 1
fib_set.add(a)

while b <= 10 ** 9:
    fib_set.add(b)
    a,b = b, a+b

print(nums)
count = sum(1 for num in nums if num in fib_set)
print(count if count > 2 else -1)