'''
Merge sort - Divide and Merge
'''

'''
Divide into 2 arrays
'''

def divide_arr(nums):
    if len(nums) == 1:
        return nums
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]
    left_arr = divide_arr(left)
    right_arr = divide_arr(right)
    return merge_arr(left_arr, right_arr)


'''
Merge 2 arrays
'''

def merge_arr(left, right):
    result = []
    i, j = 0, 0
    n, m = len(left), len(right)
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
    
    if i < n:
        while i < n:
            result.append(left[i])
            i += 1
    
    if j < m:
        while j < m:
            result.append(right[j])
            j += 1
    
    return result

nums = [4,2,7,9,3,1]
print(divide_arr(nums))