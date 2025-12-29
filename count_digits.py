import math

num = 15263

# Iterative solution
# dig_count = 0

# if num == 0:
#     print(1)

# while num != 0:
#     num = num // 10
#     dig_count += 1

# print(dig_count)

# Convert to string
# num_str = str(num)
# print(len(num_str))

print(math.floor(math.log10(num) + 1))