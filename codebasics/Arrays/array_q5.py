'''
Check if array is sorted
Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.

https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1
'''

class Solution:
    def isSorted(self, arr) -> bool:
        return arr == sorted(arr)