# 217. Contains Duplicate

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # bool1=False
        # if len(nums)>1:
        #     for index1 in range(len(nums)-1):
        #         if nums[index1]==nums[index1+1]:
        #             return True
        #     return False
        # else:
        #     return False

        # nums.sort()
        # for i in range(0, len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
    
        # return False

        # arr_set = set(nums)
        # if len(nums) != len(arr_set):
        #     return True
        # return False
        
        return len(nums) != len(set(nums))