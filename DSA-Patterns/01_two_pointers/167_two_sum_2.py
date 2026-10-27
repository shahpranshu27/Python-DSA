"""
167. Two Sum II - Input Array Is Sorted
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        index1 = 0
        index2 = len(numbers)-1
        while index1 < index2:
            two_sum = numbers[index1] + numbers[index2]
            if two_sum == target:
                return index1+1, index2+1
            if two_sum > target:
                index2 -= 1
            else:
                index1 += 1
"""
Time Complexity -->> O(N)
Sapce Complexity -->> O(1)

"""