# Hashing

# NUMBER HASHING

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

'''
Constraints:
1. 1 <= n[i] <= 10
2. n can have max 10^8 elements
3. m can have max 10^8 elements
'''

# Brute force

# for num in n:
#     for x in m:
#         if x == num:
#             print(x)
# TIME COMPLEXITY -> O(N**2)

# Optimal solution
'''
Using constraint 1, we can create a pre-filled array from numbers 1 to 10
'''
# hash_list = [0] * 11

# for num in n:
#     hash_list[num] += 1

# print(hash_list)

# for num in m:
#     if num < 1 or num > 10:
#         continue
#     else:
#         print(num, " ", hash_list[num])
# TIME COMPLEXITY -> O(N+M) -->> ~ O(N)

# Using dictionary
d = {}

for num in n:
    d[num] = d.get(num, 0) + 1

print(d)

for num in m:
    if num in d:
        print(num, " ", d[num])