"""
11 - Container with most water
"""
# TC -> O(N)
# SC -> O(1)

class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Brute Force
        # result = 0
        # for left in range(len(height)):
        #     for right in range(left+1, len(height)):
        #         area = (right - left) * min(height[left], height[right])
        #         result = max(result, area)
        
        # return result

        result = 0
        left, right = 0, len(height)-1
        while left < right:
            area = (right-left) * min(height[left], height[right])
            result = max(result, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return result