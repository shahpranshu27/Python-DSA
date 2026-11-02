"""
344 - Reverse String
"""

# TC -> O(N)
# SC -> O(1)

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        while left < len(s)/2:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1