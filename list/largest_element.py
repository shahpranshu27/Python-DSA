# https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1


class Solution:
    def largest(self, arr):
        arr.sort()
        return arr[-1]
