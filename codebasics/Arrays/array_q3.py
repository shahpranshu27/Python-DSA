'''
Largest Element in Array
Given an array arr[]. The task is to find the largest element and return it.

https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1
'''

class Solution:
    def largest(self, arr):
        max_el = arr[0]
        for i in range (0, len(arr)):
            if arr[i] > max_el:
                max_el = arr[i]
        
        return max_el
        
        # return max(arr)
        
        # arr.sort()
        
        # return (arr[-1])