# 1. Two Sum

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0, len(nums)-1):
        #     for j in range(1, len(nums)):
        #         if (nums[i] + nums[j] == target) and (i!=j):
        #             return [i, j]

        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        
        A.sort()
        
        i, j = 0, len(nums)-1
        while (i<j):
            curr = A[i][0] + A[j][0]
            if curr == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            if curr < target:
                i+=1
            else:
                j-=1

        return [i, j]