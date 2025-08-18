# https://www.geeksforgeeks.org/problems/print-alternate-elements-of-an-array/1


class Solution:
    def getAlternates(self, arr):
        arr1 = []
        for i in range(0, len(arr), 2):
            arr1.append(arr[i])

        return arr1
