'''
Array Search
Given an array, arr[] of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.

http://geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1

'''

'''
arr = [1,2,3,4,5]
x = 4

try:
    print(arr.index(x))
except:
    print(-1)

'''

class Solution:
    def search(self, arr, x):
                
        # for i in range(0, len(arr)):
        #     if arr[i] == x:
        #         return i
        
        # return -1
        
        try:
            return arr.index(x)
        except ValueError:
            return -1