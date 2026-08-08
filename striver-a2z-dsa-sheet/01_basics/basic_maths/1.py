# count digits
import math
n = int(input("enter n: "))

# cnt = 0

# while n > 0:
#     cnt += 1
#     n = n // 10

# print(cnt)

print(round(math.log10(n)+1))