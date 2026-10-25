'''
Insertion sort

take an element key which is arr[i]
j = i-1
then, compare that key element with arr[j]

if arr[j] > key: >> arr[j+1] = arr[j] and j-= 1
otherwise, arr[j+1] = key

Time Complexity --> O(N^2)
Space Complexity --> O(1)
'''

def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i-1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        
        nums[j+1] = key
    return nums

nums = [4,1,7,9,5,2]
print(insertion_sort(nums))