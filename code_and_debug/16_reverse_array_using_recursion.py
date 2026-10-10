# Reverse an array using Functional Recursion

'''
Reverse an array using Recursion
'''

def func(arr, left, right):
    if left >= right:
        return arr
    arr[left], arr[right] = arr[right], arr[left]
    return func(arr, left+1, right-1)

arr = [1,4,2,7,9,3,6,8]
print(func(arr, 0, len(arr)-1))