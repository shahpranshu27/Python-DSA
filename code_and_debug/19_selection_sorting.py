'''
Selection Sort Algorithm

take the i and j indices, where j = i+1
take the min_index = i

iterate the whole array with j loop and if any element with j index is lower than min_index element, then assign min_index to that j index

then after the min_index is assigned, continue with j, and if any element with j index found lower than min_index, assign min_index to that j index

when the first iterate loop is over, swap the elements at i and min_index, then the smallest element from the array will be at the beginning 
arr[min_index], arr[i] = arr[i], arr[min_index]

Time Complexity --> O(N^2)
Space Complexity --> O(1)

'''

'''
Selection Sort - Ascending order
'''

# def func(nums):
#     n = len(nums)
#     for i in range(n):
#         min_index = i
#         for j in range(i+1, n):
#             if nums[min_index] > nums[j]:
#                 min_index = j
#         nums[i], nums[min_index] = nums[min_index], nums[i]
#     return nums

# nums = [5,2,9,1,4,6,3,8,7]
# print(func(nums))


'''
Selection sort - Descending order
'''

def func(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if nums[min_index] < nums[j]:
                min_index = j
        
        nums[min_index], nums[i] = nums[i], nums[min_index]
    return nums

nums = [5,2,9,1,4,6,3,8,7]
print(func(nums))