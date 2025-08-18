# https://www.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1


class Solution:
    def search(self, arr, x):
        for i in range(len(arr)):
            if x == arr[i]:
                return i
            break
        return -1
