# Factors
import math

num = 100
arr = []

# brute force
# for i in range(1, num+1):
#     if num%i == 0:
#         arr.append(i)
        
# print(arr)

# better solution
# for i in range(1, num+1//2):
#     if num % i == 0:
#         arr.append(i)
# arr.append(num)

# print(arr)


# optimal solution - square root

for i in range(1, int(math.sqrt(num))+1):
    if num % i == 0:
        arr.append(i)
        if num // i != i:
            arr.append(num//i)

print(arr)