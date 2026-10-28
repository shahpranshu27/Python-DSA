"""
125. Valid Palindrome

TC -> O(N)
SC -> O(N) since .lower() creates a new string
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char for char in s if char.isalnum()])
        s = s.lower()

        i = 0
        j = len(s)-1
        while i < len(s)/2:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True