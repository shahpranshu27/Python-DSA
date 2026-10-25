'''
Bubble Sort - Adjacent swapping elements

Start with the first element, and check the j and j+1, if the arr[j+1] > arr[j], then swap

Time Complexity --> O(N^2) [Worst Case]
                    O(N) [Best Case])
Space Complexity --> O(1)
'''

def sort_arr(nums):
    n = len(nums)
    for i in range(n-2, -1, -1):
        for j in range(0, i+1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return nums

nums = [3,6,1,7,9,2]
print(sort_arr(nums))