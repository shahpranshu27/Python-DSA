"""
Valid anagrams - Leetcode 242
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # s = "".join(sorted(s))
        # t = "".join(sorted(t))

        # return s == t

        # dict1 = {}
        # dict2 = {}

        # for i in s:
        #     dict1[i] = dict1[i]+1 if i in dict1 else 1
        
        # for j in t:
        #     dict2[j] = dict2[j]+1 if j in dict2 else 1
        
        # return (dict1 == dict2)

        # dict1 = {}
        # dict2 = {}

        # for i in s:
        #     dict1[i] = dict1.get(i, 0) + 1
        
        # for i in t:
        #     dict2[i] = dict2.get(i, 0) + 1
        
        # return dict1 == dict2

        # return sorted(s) == sorted(t)

        d1 = {}
        d2 = {}

        for i in s:
            d1[i] = d1.get(i, 0) + 1
        for j in t:
            d2[j] = d2.get(j, 0) + 1
        
        return d1 == d2