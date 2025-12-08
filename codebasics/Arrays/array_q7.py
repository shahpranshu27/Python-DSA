'''
Third largest element
Given an array, arr of positive integers. Find the third largest element in it. Return -1 if the third largest element is not found.
https://www.geeksforgeeks.org/problems/third-largest-element/1
'''

class Solution:
    def thirdLargest(self,arr):
        if len(arr) < 3:
            return -1
        
        arr.sort(reverse=True)
        arr = list(set(arr))
        return arr[2]