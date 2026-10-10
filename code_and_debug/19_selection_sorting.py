'''
Selection Sort - Ascending order
'''

def func(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

nums = [5,2,9,1,4,6,3,8,7]
print(func(nums))