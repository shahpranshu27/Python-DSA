# reverse an array

def printArr(arr):
    for i in range(0, len(arr)):
        print(arr[i], end=" ")

def reverseArr(arr):
    arr.reverse()

arr = [1,2,3]
printArr(arr)
reverseArr(arr)
print("\n")
printArr(arr)