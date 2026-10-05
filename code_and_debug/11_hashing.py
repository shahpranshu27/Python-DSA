# Hashing

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

'''
Constraints:
1. 1 <= n[i] <= 10
2. n can have max 10^8 elements
3. m can have max 10^8 elements
'''

# Brute force

for num in n:
    for x in m:
        if x == num:
            print(x)

# TIME COMPLEXITY -> O(N**2)