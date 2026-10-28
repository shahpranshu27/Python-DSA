"""
26. Remove Duplicates from Sorted Array
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        j = i+1
        while j < len(nums) and i < j:
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i+1] = nums[j]
                i+= 1
                j+= 1

        return i+1