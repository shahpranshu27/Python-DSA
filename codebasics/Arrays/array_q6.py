'''
Second Largest
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
https://www.geeksforgeeks.org/problems/second-largest3735/1
'''

class Solution:
    def getSecondLargest(self, arr):
        arr.sort()
        max_el = arr[-1]
        for i in range(len(arr)-1, -1, -1):
            if (arr[i] < max_el):
                max_el = arr[i]
                return max_el

        return -1