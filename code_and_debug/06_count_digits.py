# Count Digits

from math import *

num = 5873
count = 0

# while num > 0:
#     count += 1
#     num = num // 10

# print(count)

print(int(log10(num) + 1))