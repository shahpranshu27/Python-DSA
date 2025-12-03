'''
Alternates in an Array
You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0).

https://www.geeksforgeeks.org/problems/print-alternate-elements-of-an-array/1
'''

arr = [1,2,3,4,5]
arr2 = []

# Brute force
# for i in range (0, len(arr)):
#     if i%2 == 0:
#         print(i)
#         arr2.append(arr[i])

# Optimised
for i in range (0, len(arr), 2):
    arr2.append(arr[i])

print(arr2)