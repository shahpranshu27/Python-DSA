# 1929. Concatenation of Array

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = 2 * nums
        # return ans

        # ans = []
        # for i in range(2):
        #     for num in nums:
        #         ans.append(num)
        # return ans

        # n = len(nums)
        # ans = [0] * 2*n
        # for i, num in enumerate(nums):
        #     ans[i] = ans[i+n] = num
        # return ans

        # return 2*nums

        # ans = []
        # for index in range(2):
        #     for i, num in enumerate(nums):
        #         ans.insert(i, num)
        
        # return ans

        ans = []
        for _ in range(2):
            for num in nums:
                ans.append(num)
        
        return ans