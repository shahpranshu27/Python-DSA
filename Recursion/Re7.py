# reverse an array

def printArr(arr):
    for i in range(0, len(arr)):
        print(arr[i], end=" ")

# def reverseArr(arr):
#     arr.reverse()

# arr = [1,2,3]
# printArr(arr)
# reverseArr(arr)
# print("\n")
# printArr(arr)

def reverseArr(arr, start, end):
    if start<end:
        arr[start], arr[end] = arr[end], arr[start]
        reverseArr(arr, start+1, end-1)

arr = [1,2,4,5,3]
printArr(arr)
n = len(arr)
reverseArr(arr, 0, n-1)
print('\n')
printArr(arr)